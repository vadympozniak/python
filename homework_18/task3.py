"""Write a class TypeDecorators which has several methods for converting results
of functions to a specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float
Don't forget to use @wraps"""

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            x = func(*args, **kwargs)
            if x.isdigit():
                return int(x)
            else:
                raise ValueError

        return wrap

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            x = func(*args, **kwargs)
            return str(x)

        return wrap

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            x = func(*args, **kwargs)
            return bool(x)

        return wrap

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            x = func(*args, **kwargs)
            try:
                return float(x)
            except:
                raise ValueError

        return wrap


@TypeDecorators.to_int
def do_int(string: str):
    return string


@TypeDecorators.to_str
def do_str(string: str):
    return string


@TypeDecorators.to_bool
def do_bool(string):
    return string


@TypeDecorators.to_float
def do_float(string: str):
    return string


if __name__ == '__main__':
    print(do_int('12'))
    print(do_str('str'))
    print(do_bool(''))
    print(do_bool('12'))
    print(do_float('12'))
    print(do_float('0'))