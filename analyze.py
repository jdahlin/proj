import ast

builtins = """
class file(object):
    def read(self, size=-1):
        pass
    read.retval = str

def open(name, mode='r', buffering=0):
    pass
open.retval = file
"""

class Call(object):
    def __init__(self, node):
        self.call = node
        self.func_name = None
        self.type = None

    def resolve(self, namespace):
        func = self.call.func
        if isinstance(func, ast.Name):
            self.func_name = func.id
        elif isinstance(func, ast.Attribute):
            try:
                target = namespace[func.value.id]
            except KeyError:
                return
            print 'attr', target
        else:
            raise NotImplementedError(self.call)


class Visitor(ast.NodeVisitor):
    def __init__(self):
        ast.NodeVisitor.__init__(self)
        self.namespace = {}
        self.callers = []

    def visit_Call(self, node):
        call = Call(node)
        call.resolve(self.namespace)
        self.callers.append(call)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node):
        for target in node.targets:
            self.namespace[target.id] = node.value.func
        ast.NodeVisitor.generic_visit(self, node)


def test_simple():
    tree = ast.parse("f = func()")
    v = Visitor()
    v.visit(tree)
    assert len(v.callers) == 1
    assert v.callers[0].func_name == 'func'


def test_indirected():
    tree = ast.parse("""
fd = open("foo")
fd.read()""")
    v = Visitor()
    v.visit(tree)


if __name__ == '__main__':
    test_simple()
    test_indirected()
