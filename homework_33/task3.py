"""One way to improve the quicksort is to use an insertion sort on lists that are
small in length (call it the “partition limit”). Why does this make sense?
Re-implement the quicksort and use it to sort a random list of integers.
Perform analysis using different list sizes for the partition limit."""


import random


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    random_list = random.sample(range(1, 30), 10)
    print(random_list)
    quick_sort(random_list)
    print(random_list)