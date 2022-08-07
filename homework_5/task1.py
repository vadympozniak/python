"""The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess
what number was generated. The result should be sent back to the user via a print statement."""


import random


random_number = random.randint(1, 10)
user_number = input('Enter the  number between 1 and 10: ')

while not user_number.isdigit() or int(user_number) < 1 or int(user_number) > 10:
    user_number = input('Number is incorrect. Please, enter the  number between 1 and 10:')

if int(user_number) == random_number:
    print(f"You guessed it. It's a number {user_number}.")
else:
    print(f"You didn't guess it. it's a number. {random_number}.")

