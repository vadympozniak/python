"""A Person class
Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes. Make another method called talk() which makes
prints a greeting from the person containing, for example like this:
“Hello, my name is Carl Johnson and I’m 26 years old”."""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        if str(self.age).isdigit():
            print(f'Hello, my name is {self.first_name} {self.last_name} and I\'m {self.age} years old')
        else:
            print('Age is not number.')


if __name__ == '__main__':
    man = Person('Carl', 'Johnson', 26)
    man.talk()