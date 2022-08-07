"""Words combination
Create a program that reads an input string and then creates and prints 5 random strings
from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
that combine characters """

import random

word = input('Enter a word with more than 5 letters:')

while len(word) < 5:
    word = input('Please, Enter a word with more than 5 letters:')

word_list = list(word.lower())

collect_words = []

while len(collect_words) < 5:
    random.shuffle(word_list)
    one_word = ''.join(word_list)
    if (one_word not in collect_words) and (one_word != word):
        collect_words.append(one_word)

print(collect_words)
