"""Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function"""


def in_range(start, end, optional_step):
    if str(start).isalpha() or str(end).isalpha() or str(optional_step).isalpha():
        print('Enter a number')

    else:
        func_start = int(str(start))
        func_end = int(str(end))
        func_optional_step = int(str(optional_step))

        if (func_start > func_end) and (func_optional_step > 0):
            print(f'Incorrect data. First number  ({func_start}) greater than last one ({func_end}) '
                  f'with step ({func_optional_step}).')
        elif (func_start < func_end) and (func_optional_step < 0):
            print(f'Incorrect data. First number ({func_start}) less than last one ({func_end}) '
                  f'with step ({func_optional_step}).')

        else:
            i = func_start
            while abs(i) < abs(func_end):
                yield i
                i += func_optional_step


if __name__ == '__main__':
    list_1 = in_range(100, 120, 3)
    for num in list_1:
        print(f'Numbers of the 1 operation — {num}')
    print()

    list_2 = in_range(120, 100, 3)
    for num in list_2:
        print(f'Numbers of the 2 operation  — {num}')
    print()

    list_3 = in_range(-100, 120, -3)
    for num in list_3:
        print(f'Numbers of the 3 operation  — {num}')
    print()

    list_4 = in_range(100, -120, -3)
    for num in list_4:
        print(f'Numbers of the 4 operation  — {num}')
    print()
