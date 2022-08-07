"""The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers"""

import random


random_list = random.sample(range(1, 100), 10)

print(max(random_list))
