"""The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years"""


name = input('Enter your name:')
while not name.isalpha():
    name = input('Name is incorrect.Enter your name:')

age = input('Enter your age:')
while not age.isdigit() or int(age) < 0:
    age = input('Age is incorrect.Enter your age:')

print(f"Hello {name}, on your next birthday you’ll be {int(age)+1} years.")
