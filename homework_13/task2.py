"""Write a Python program to access a function inside a function (Tips: use function, which returns another function)"""


def number(a):
    return a


def square(b):
    def result_square(c):
        return b(c) ** 2
    return result_square


result = square(number)

print(result(100))
