def baz():
    return 'string'
def bar():
    return baz()
def foo():
    return bar()
ret = foo()
f = open("/proc/meminfo")
#data = f.readlines()
print len('')
