"""Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?"""


def oops():
    raise IndexError('IndexError')


def function():
    try:
        oops()
    except IndexError as text_error:
        print(f'{text_error}')


if __name__ == '__main__':
    print(function())