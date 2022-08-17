"""Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function"""


import itertools


def with_index(iterable_, start_=0):
    if str(start_).isalpha():
        print('Enter a number')
    else:
        list_ = list(zip(itertools.count(start=int(str(start_))), iterable_))
        return list_


if __name__ == '__main__':
    number = ('one', 'two', 'three')
    with_index_fruits = with_index(number, 1)
    print(with_index_fruits)