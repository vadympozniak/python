"""Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero)."""


def function():
    while True:
        a = input("Enter the first number:")
        b = input("Enter the second number:")
        try:
            c = int(a) ** 2 / int(b)
        except ValueError:
            print("You have entered non-numeric values")
        except ZeroDivisionError:
            print("The second number cannot be 0")
        else:
            return c


if __name__ == '__main__':
    print(function())