"""A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate."""


import random


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

                print(nums)


if __name__ == "__main__":
    random_list = random.sample(range(1, 30), 10)
    print(random_list)
    bubble_sort(random_list)
    print(random_list)