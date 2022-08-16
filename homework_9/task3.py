"""A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator
as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number
of arguments (only numbers) as the second parameter. Then return the sum or product of all
the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  """


def make_operation(operation, *args):
    if operation != '+' and operation != '-' and operation != '*':
        result = "You have entered an invalid operator, required : '+', '-' або '*'"
    else:
        result = args[0]
        for i in range(1, len(args)):
            if operation == '+':
                result += args[i]
            elif operation == '-':
                result -= args[i]
            else:
                result *= args[i]
    return result


if __name__ == '__main__':
    print(make_operation('+', 7, 7, 2))
    print(make_operation('-', 5, 5, -10, -20))
    print(make_operation('*', 7, 6))