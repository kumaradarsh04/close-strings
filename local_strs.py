import keyword
import builtins
import types

result = []

kwlist = []
for kw in keyword.kwlist:
    result.append(kw)

# built-in functions
functions = []
for name in dir(builtins):
    obj = getattr(builtins, name)
    if isinstance(obj, types.BuiltinFunctionType):
        result.append(name)
        functions.append(name)


# all built-in exceptions
exceptions = []
for name in dir(builtins):
    obj = getattr(builtins, name)
    if isinstance(obj, type) and issubclass(obj, BaseException):
        result.append(name)
        exceptions.append(name)


is_keyword = keyword.iskeyword
is_exception_name = frozenset(exceptions).__contains__
is_bltn_function = frozenset(functions).__contains__

keywords = result.copy()
