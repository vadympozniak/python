"""Write a Python program to detect the number of local variables declared in a function."""


import random


def function():
    variables = random.randint(1, 10)
    list_variables = []
    for i in range(variables):
        list_variables.append(i)


print(f'Number of local variables — {function.__code__.co_nlocals}.')