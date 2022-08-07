"""Basics, import, work with os module

Write a program that counts lines and characters in a file.
Create a Python module called `mymod.py`, which has three functions:

count_lines(name) function that reads an input file and counts the number of lines in it (hint: file.readlines()
does most of the work for you, and `len` does the rest)
count_chars(name) function that reads an input file and counts the number of characters in it (hint: file.read()
returns a single string)
test(name) function that calls both counting functions with a given input filename.
Such a filename generally might be passed-in, hard-coded, input with raw_input, or pulled
from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
All three `mymod.py` functions should expect a filename string to be passed in.

Test your module interactively, using import and name qualification to fetch your exports.

Does your PYTHONPATH need to include the directory where you created mymod.py?

Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice;
if you’re feeling ambitious, you may be able to improve this by passing an open file object
into the two count functions (hint: file.seek(0) is a file rewind)."""


def count_lines(name):
    try:
        with open(name, 'r') as filename:
            lines = filename.readlines()
        return len(lines)
    except FileNotFoundError:
        print('File is not found.')


def count_chars(name):
    try:
        with open(name, 'r') as filename:
            string = filename.read()
        return len(string)
    except FileNotFoundError:
        print('File is not found')


def test(name):
    return f'Rows — {count_lines(name)}, sings — {count_chars(name)}.'


if __name__ == '__main__':
    print(count_lines('text.txt'))
    print(count_chars('text.txt'))
    print(test('text.txt'))
