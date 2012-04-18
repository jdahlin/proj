import ast
import types

import builtins


class Function(object):
    def __init__(self, name, args, rettype):
        self.name = name
        self.args = args
        self.rettype = rettype


class Reference(object):
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def __repr__(self):
        return 'Reference(%r)' % (self.value, )


class TypeInfo(object):
    def __init__(self, node, value):
        assert not type(value) is TypeInfo
        self.node = node
        self.value = value

    def __repr__(self):
        return 'TypeInfo(%r)' % (self.value, )


class Module(object):
    def __init__(self):
        pass


class Scope(object):
    def __init__(self):
        self.scopes = []

    def lookup(self, attr):
        for scope in reversed(self.scopes):
            if hasattr(scope, attr):
                return getattr(scope, attr)

        raise AttributeError(attr)

    def push(self, scope):
        self.scopes.append(scope)

    def pop(self):
        del self.scopes[-1]


class Visitor(ast.NodeVisitor):
    #
    # A) Figure out which external parts this
    #    piece of code references
    # B) Attach type information to variables
    #
    def __init__(self):
        ast.NodeVisitor.__init__(self)
        self.module = Module()
        self.scope = Scope()
        self.scope.push(builtins)
        self.scope.push(self.module)
        self.namespace = {}

        # List of references to outside of this block of code
        self.references = {}

    def visit_Name(self, node):
        if not isinstance(node.ctx, ast.Load):
            return
        if node.id not in self.namespace:
            attr = self.scope.lookup(node.id)
            self.references[node.id] = Reference(node, attr)

    def visit_Assign(self, node):
        ast.NodeVisitor.visit(self, node.value)
        if isinstance(node.value, ast.Call):
            type_info = node.value.type_info
        elif isinstance(node.value, ast.Name):
            type_info = self.namespace[node.value.id]
        else:
            guess_type = self._guess_type(node.value)
            if guess_type is None:
                raise NotImplementedError(node.value)
            type_info = TypeInfo(node.value, guess_type)

        for target in node.targets:
            setattr(self.module, target.id, node.value)
            self.namespace[target.id] = type_info
            ast.NodeVisitor.visit(self, target)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            obj = self.scope.lookup(node.func.id)
            if isinstance(obj, Function):
                type_info = obj.rettype
            elif isinstance(obj, types.FunctionType):
                rettype = getattr(obj, 'rettype', None)
                if rettype is not None:
                    type_info = TypeInfo(node.func, rettype)
            else:
                type_info = TypeInfo(node.func, obj)
        elif isinstance(node.func, ast.Attribute):
            live_parent = self.namespace[node.func.value.id]
            live_obj = getattr(live_parent.value, node.func.attr, None)
            self.references[node.func.attr] = Reference(node.func, live_obj)
            type_info = TypeInfo(node.func, live_obj.rettype)
        elif isinstance(node.func, ast.Subscript):
            type_info = None
        else:
            raise NotImplementedError(node.func)
        node.type_info = type_info
        ast.NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        returns = []
        for stmt in node.body:
            if isinstance(stmt, ast.Return):
                returns.append(stmt)

        if len(returns) == 0:
            rettype = TypeInfo(None, None)
        elif len(returns) == 1:
            ret_node = returns[0]
            value = self._guess_type(ret_node.value)
            rettype = TypeInfo(ret_node, value)
        else:
            raise NotImplementedError("several returns")

        func = Function(name=node.name,
                        args=node.args.args,
                        rettype=rettype)
        setattr(self.module, node.name, func)
        self.namespace[node.name] = func

    def _guess_type(self, node):
        if isinstance(node, ast.Str):
            return type(node.s)
        elif isinstance(node, ast.Num):
            return type(node.n)
        elif isinstance(node, ast.Call):
            type_info = self.namespace[node.func.id]
            return type_info.rettype.value
        else:
            raise NotImplementedError(node)

def analyze(text, filename="<stdin>"):
    try:
        tree = compile(text, filename, 'exec', ast.PyCF_ONLY_AST)
    except SyntaxError, value:
        left = text.count('(')
        right = text.count(')')
        while left > right:
            text += ')'
            right += 1
        tree = ast.parse(text)
    visitor = Visitor()
    visitor.visit(tree)
    return visitor


def test_simple():
    v = analyze("f = open()")
    assert v.namespace['f'].value == builtins.file
    assert v.references['open'].value == builtins.open


def test_basic_types():
    v = analyze("""
str = "foo"
int = 1
long = 1L
float = 1.0
unicode = u'unicode'""")
    assert v.namespace['str'].value == str
    assert v.namespace['int'].value == int
    assert v.namespace['long'].value == long
    assert v.namespace['float'].value == float
    assert v.namespace['unicode'].value == unicode


def test_indirected():
    tree = ast.parse("""
fd = open("foo")
fd.read()""")
    v = Visitor()
    v.visit(tree)
    assert v.references['open'].value == builtins.open
    assert v.references['read'].value == builtins.file.read
    assert v.namespace['fd'].value == builtins.file


def test_multi_assignment():
    v = analyze("""
a = open("foo")
b = a
c = b
d = c""")
    assert v.namespace['a'].value == builtins.file
    assert v.namespace['b'].value == builtins.file
    assert v.namespace['c'].value == builtins.file
    assert v.namespace['d'].value == builtins.file

def test_recursive_attributes():
    v = analyze("""
a = open("foo")
b = a
c = b
d = c""")
    assert v.namespace['a'].value == builtins.file
    assert v.namespace['b'].value == builtins.file
    assert v.namespace['c'].value == builtins.file
    assert v.namespace['d'].value == builtins.file

def test_function():
    v = analyze("""
def function():
    return 'foobar'
a = function()
""")
    func = v.namespace['function']
    assert func.args == []
    assert func.rettype.value == str, func.rettype
    assert v.namespace['a'].value == str, v.namespace['a'].value

def test_function():
    v = analyze("""
def baz():
    return 'string'
def bar():
    return baz()
def foo():
    return bar()
ret = foo()
""")
    func = v.namespace['foo']
    assert func.args == []
    assert func.rettype.value == str, func.rettype
    func = v.namespace['bar']
    assert func.args == []
    assert func.rettype.value == str, func.rettype
    func = v.namespace['baz']
    assert func.args == []
    assert func.rettype.value == str, func.rettype
    assert v.namespace['ret'].value == str, v.namespace['ret'].value

def test_partial_function_call():
    v = analyze("open(")
    assert v.references['open'].value == builtins.open

    v = analyze("open(str(")
    assert v.references['open'].value == builtins.open
    assert v.references['str'].value == builtins.str


def test_non_function_reference():
    v = analyze("str[hash](id)")
    assert v.references['str'].value == builtins.str
    assert v.references['hash'].value == builtins.hash
    assert v.references['id'].value == builtins.id


if __name__ == '__main__':
    test_simple()
    test_basic_types()
    test_indirected()
    test_multi_assignment()
    test_function()
    test_partial_function_call()
    test_non_function_reference()
