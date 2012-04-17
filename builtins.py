import sys
import types


class basestring:
    """Type basestring cannot be instantiated; it is the base for str and unicode."""


class bool:
    """bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed."""


class bytearray:
    """bytearray(iterable_of_ints) -> bytearray.
bytearray(string, encoding[, errors]) -> bytearray.
bytearray(bytes_or_bytearray) -> mutable copy of bytes_or_bytearray.
bytearray(memory_view) -> bytearray.

Construct an mutable bytearray object from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - a bytes or a bytearray object
  - any object implementing the buffer API.

bytearray(int) -> bytearray.

Construct a zero-initialized bytearray of the given length."""


class bytes:
    """str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object."""


class classmethod:
    """classmethod(function) -> method

Convert a function to be a class method.

A class method receives the class as implicit first argument,
just like an instance method receives the instance.
To declare a class method, use this idiom:

  class C:
      def f(cls, arg1, arg2, ...): ...
      f = classmethod(f)

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()).  The instance is ignored except for its class.
If a class method is called for a derived class, the derived class
object is passed as the implied first argument.

Class methods are different than C++ or Java static methods.
If you want those, see the staticmethod builtin."""


class complex:
    """complex(real[, imag]) -> complex number

Create a complex number from a real part and an optional imaginary part.
This is equivalent to (real + imag*1j) where imag defaults to 0."""


class dict:
    """dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)"""


class file:
    """file(name[, mode[, buffering]]) -> file object

Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
writing or appending.  The file will be created if it doesn't exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a 'b' to the mode for binary files.
Add a '+' to the mode to allow simultaneous reading and writing.
If the buffering argument is given, 0 means unbuffered, 1 means line
buffered, and larger numbers specify the buffer size.  The preferred way
to open a file is with the builtin open() function.
Add a 'U' to mode to open the file for input with universal newline
support.  Any line ending in the input file will be seen as a '\n'
in Python.  Also, a file so opened gains the attribute 'newlines';
the value for this attribute is one of None (no newline read yet),
'\r', '\n', '\r\n' or a tuple containing all the newline types seen.

'U' cannot be combined with 'w' or '+' mode.
"""

    def read(self, size=-1):
        pass
    read.rettype = str


class float:
    """float(x) -> floating point number

Convert a string or number to a floating point number, if possible."""


class frozenset:
    """frozenset() -> empty frozenset object
frozenset(iterable) -> frozenset object

Build an immutable unordered collection of unique elements."""


class int:
    """int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead."""


class list:
    """list() -> new empty list
list(iterable) -> new list initialized from iterable's items"""

    def __init__(self, iterable=None):
        pass

    def append(self, item):
        pass


class long:
    """long(x[, base]) -> integer

Convert a string or number to a long integer, if possible.  A floating
point argument will be truncated towards zero (this does not include a
string representation of a floating point number!)  When converting a
string, use the optional base.  It is an error to supply a base when
converting a non-string."""

    def __init__(self, x, base=None):
        pass


class object:
    """The most base type"""


class property:
    """property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

fget is a function to be used for getting an attribute value, and likewise
fset is a function for setting, and fdel a function for del'ing, an
attribute.  Typical use is to define a managed attribute x:
class C(object):
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

Decorators make defining new properties or modifying existing ones easy:
class C(object):
    @property
    def x(self): return self._x
    @x.setter
    def x(self, value): self._x = value
    @x.deleter
    def x(self): del self._x
""" #'
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        pass


class set:
    """set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements."""
    def __init__(self, iterable=None):
        pass


class staticmethod:
    """staticmethod(function) -> method

Convert a function to be a static method.

A static method does not receive an implicit first argument.
To declare a static method, use this idiom:

     class C:
     def f(arg1, arg2, ...): ...
     f = staticmethod(f)

It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()).  The instance is ignored except for its class.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin."""
    def __init__(self, function=None):
        pass


class str:
    """str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object."""
    def __init__(self, object=None):
        pass


class super:
    """super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super(C, self).meth(arg)"""


class type:
    """type(object) -> the object's type
type(name, bases, dict) -> a new type"""


class unicode:
    """unicode(string [, encoding[, errors]]) -> object

Create a new Unicode object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'."""
    def __init__(self, string, encoding=None, errors='strict'):
        pass


def __import__(name, globals={}, locals={}, fromlist=[], level=-1):
    """__import__(name, globals={}, locals={}, fromlist=[], level=-1) -> module

Import a module.  The globals are only used to determine the context;
they are not modified.  The locals are currently unused.  The fromlist
should be a list of names to emulate ``from name import ...'', or an
empty list to emulate ``import name''.
When importing a module from a package, note that __import__('A.B', ...)
returns package A when fromlist is empty, but its submodule B when
fromlist is not empty.  Level is used to determine whether to perform
absolute or relative imports.  -1 is the original strategy of attempting
both absolute and relative imports, 0 is absolute, a positive number
is the number of parent directories to search relative to the current module."""


def abs(number):
    """abs(number) -> number

Return the absolute value of the argument."""


def all(iterable):
    """all(iterable) -> bool

Return True if bool(x) is True for all values x in the iterable."""
all.rettype = bool


def any(iterable):
    """any(iterable) -> bool

Return True if bool(x) is True for any x in the iterable."""
any.rettype = bool


def apply(object, args=None, kwargs=None):
    """apply(object[, args[, kwargs]]) -> value

Call a callable object with positional arguments taken from the tuple args,
and keyword arguments taken from the optional dictionary kwargs.
Note that classes are callable, as are instances with a __call__() method.

Deprecated since release 2.3. Instead, use the extended call syntax:
    function(*args, **keywords)."""


def bin(number):
    """bin(number) -> string

Return the binary representation of an integer or long integer."""
bin.rettype = str


def buffer(object, offset=-1, size=-1):
    """buffer(object [, offset[, size]])

Create a new buffer object which references the given object.
The buffer will reference a slice of the target object from the
start of the object (or at the specified offset). The slice will
extend to the end of the target object (or with the specified size)."""


def callable(object):
    """callable(object) -> bool

Return whether the object is callable (i.e., some kind of function).
Note that classes are callable, as are instances with a __call__() method."""
callable.rettype = bool


def chr(i):
    """chr(i) -> character

Return a string of one character with ordinal i; 0 <= i < 256."""
chr.rettype = str


def cmp(x, y):
    """cmp(x, y) -> integer

Return negative if x<y, zero if x==y, positive if x>y."""
cmp.rettype = int


def coerce(x, y):
    """coerce(x, y) -> (x1, y1)

Return a tuple consisting of the two numeric arguments converted to
a common type, using the same rules as used by arithmetic operations.
If coercion is not possible, raise TypeError."""


def compile(source, filename, mode, flags=0, dont_inherit=0):
    """compile(source, filename, mode[, flags[, dont_inherit]]) -> code object

Compile the source string (a Python module, statement or expression)
into a code object that can be executed by the exec statement or eval().
The filename will be used for run-time error messages.
The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.
The flags argument, if present, controls which future statements influence
the compilation of the code.
The dont_inherit argument, if non-zero, stops the compilation inheriting
the effects of any future statements in effect in the code calling
compile; if absent or zero these statements do influence the compilation,
in addition to any features explicitly specified."""
compile.rettype = types.CodeType


def copyright():
    """interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice."""


def credits():
    """interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice."""


def delattr(object, name):
    """delattr(object, name)

Delete a named attribute on an object; delattr(x, 'y') is equivalent to
``del x.y''."""


def dir(object=None):
    """dir([object]) -> list of strings

If called without an argument, return the names in the current scope.
Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.
If the object supplies a method named __dir__, it will be used; otherwise
the default dir() logic is used and returns:
  for a module object: the module's attributes.
  for a class object:  its attributes, and recursively the attributes
    of its bases.
  for any other object: its attributes, its class's attributes, and
    recursively the attributes of its class's base classes."""
dir.rettype = list


def divmod(x, y):
    """divmod(x, y) -> (quotient, remainder)

Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x."""


def enumerate(iterable, start):
    """enumerate(iterable[, start]) -> iterator for index, value of iterable

Return an enumerate object.  iterable must be another object that supports
iteration.  The enumerate object yields pairs containing a count (from
start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ..."""


def eval(source, globals=None, locals=None):
    """eval(source[, globals[, locals]]) -> value

Evaluate the source in the context of globals and locals.
The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.
"""


def execfile(filename, globals=None, locals=None):
    """execfile(filename[, globals[, locals]])

Read and execute a Python script from a file.
The globals and locals are dictionaries, defaulting to the current
globals and locals.  If only globals is given, locals defaults to it."""


def filter(function, sequence):
    """filter(function or None, sequence) -> list, tuple, or string

Return those items of sequence for which function(item) is true.  If
function is None, return the items that are true.  If sequence is a tuple
or string, return the same type, else return a list."""


def format(value, format_spec=None):
    """format(value[, format_spec]) -> string

Returns value.__format__(format_spec)
format_spec defaults to """""


def getattr(object, name, default=None):
    """getattr(object, name[, default]) -> value

Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn't
exist; without it, an exception is raised in that case."""


def globals():
    """globals() -> dictionary

Return the dictionary containing the current scope's global variables."""
globals.rettype = dict


def hasattr(object, name):
    """hasattr(object, name) -> bool

Return whether the object has an attribute with the given name.
(This is done by calling getattr(object, name) and catching exceptions.)"""
hasattr.rettype = bool


def hash(object):
    """hash(object) -> integer

Return a hash value for the object.  Two objects with the same value have
the same hash value.  The reverse is not necessarily true, but likely."""
hash.rettype = int


def help():
    """Define the builtin 'help'.
    This is a wrapper around pydoc.help (with a twist).

    """


def hex(number):
    """hex(number) -> string

Return the hexadecimal representation of an integer or long integer."""
hex.rettype = str


def id(object):
    """id(object) -> integer

Return the identity of an object.  This is guaranteed to be unique among
simultaneously existing objects.  (Hint: it's the object's memory address.)"""
id.rettype = int


def input(prompt=None):
    """input([prompt]) -> value

Equivalent to eval(raw_input(prompt))."""


def intern(string):
    """intern(string) -> string

``Intern'' the given string.  This enters the string in the (global)
table of interned strings whose purpose is to speed up dictionary lookups.
Return the string itself or the previously interned string object with the
same value."""
intern.rettype = str


def isinstance(object, class_or_type_or_tuple):
    """isinstance(object, class-or-type-or-tuple) -> bool

Return whether an object is an instance of a class or of a subclass thereof.
With a type as second argument, return whether that is the object's type.
The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
isinstance(x, A) or isinstance(x, B) or ... (etc.)."""
isinstance.rettype = bool


def issubclass(C, B):
    """issubclass(C, B) -> bool

Return whether class C is a subclass (i.e., a derived class) of class B.
When using a tuple as the second argument issubclass(X, (A, B, ...)),
is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.)."""
issubclass.rettype = bool


def iter():
    """iter(collection) -> iterator
iter(callable, sentinel) -> iterator

Get an iterator from an object.  In the first form, the argument must
supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel."""


def len(object):
    """len(object) -> integer

Return the number of items of a sequence or mapping."""
len.rettype = int


def license():
    """interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice."""


def locals():
    """locals() -> dictionary

Update and return a dictionary containing the current scope's local variables."""


def map(function, *sequence):
    """map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence)."""
map.rettype = list


def max(iterable, key=None, *args):
    """max(iterable[, key=func]) -> value
max(a, b, c, ...[, key=func]) -> value

With a single iterable argument, return its largest item.
With two or more arguments, return the largest argument."""


def memoryview(object):
    """memoryview(object)

Create a new memoryview object which references the given object."""


def min(iterable, key=None, *args):
    """min(iterable[, key=func]) -> value
min(a, b, c, ...[, key=func]) -> value

With a single iterable argument, return its smallest item.
With two or more arguments, return the smallest argument."""


def next(iterator, default=None):
    """next(iterator[, default])

Return the next item from the iterator. If default is given and the iterator
is exhausted, it is returned instead of raising StopIteration."""


def oct(number):
    """oct(number) -> string

Return the octal representation of an integer or long integer."""
oct.rettype = str


def open(name, mode='r', buffering=0):
    """open(name[, mode[, buffering]]) -> file object

Open a file using the file() type, returns a file object.  This is the
preferred way to open a file.  See file.__doc__ for further information."""
open.rettype = file


def ord(c):
    """ord(c) -> integer

Return the integer ordinal of a one-character string."""
ord.rettype = int


def pow(x, y, z=None):
    """pow(x, y[, z]) -> number

With two arguments, equivalent to x**y.  With three arguments,
equivalent to (x**y) % z, but may be more efficient (e.g. for longs)."""


def range():
    """range([start,] stop[, step]) -> list of integers

Return a list containing an arithmetic progression of integers.
range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
When step is given, it specifies the increment (or decrement).
For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
These are exactly the valid indices for a list of 4 elements."""


def raw_input(prompt):
    """raw_input([prompt]) -> string

Read a string from standard input.  The trailing newline is stripped.
If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
On Unix, GNU readline is used if enabled.  The prompt string, if given,
is printed without a trailing newline before reading."""
raw_input.rettype = str


def reduce(function, sequence, initial=None):
    """reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty."""


def reload(module):
    """reload(module) -> module

Reload the module.  The module must have been successfully imported before."""


def repr(object):
    """repr(object) -> string

Return the canonical string representation of the object.
For most object types, eval(repr(object)) == object."""


def reversed(sequence):
    """reversed(sequence) -> reverse iterator over values of the sequence

Return a reverse iterator"""


def round(number, ndigits=0):
    """round(number[, ndigits]) -> floating point number

Round a number to a given precision in decimal digits (default 0 digits).
This always returns a floating point number.  Precision may be negative."""


def setattr(object, name, value):
    """setattr(object, name, value)

Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
``x.y = v''."""


def slice():
    """slice([start,] stop[, step])

Create a slice object.  This is used for extended slicing (e.g. a[0:10:2])."""


def sorted(iterable, cmp=None, key=None, reverse=False):
    """sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list"""


def sum(sequence, start=0):
    """sum(sequence[, start]) -> value

Returns the sum of a sequence of numbers (NOT strings) plus the value
of parameter 'start' (which defaults to 0).  When the sequence is
empty, returns start."""


def tuple(iterable=None):
    """tuple() -> empty tuple
tuple(iterable) -> tuple initialized from iterable's items

If the argument is a tuple, the return value is the same object."""


def unichr(i):
    """unichr(i) -> Unicode character

Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff."""
unichr.rettype = unicode


def vars(object=None):
    """vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__."""
vars.rettype = dict


def xrange():
    """xrange([start,] stop[, step]) -> xrange object

Like range(), but instead of returning a list, returns an object that
generates the numbers in the range on demand.  For looping, this is
slightly faster than range() and more memory efficient."""


def zip(*seq):
    """zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

Return a list of tuples, where each tuple contains the i-th element
from each of the argument sequences.  The returned list is truncated
in length to the length of the shortest argument sequence."""


