"""Implement the mergeSort function without using the slice operator."""

import random


def merge(left_list, right_list):
    sorted_list = []
    left_index = 0
    right_index = 0
    left_length = len(left_list)
    right_length = len(right_list)

    while left_index + right_index < left_length + right_length:
        if left_index == left_length:
            sorted_list.append(right_list[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted_list.append(left_list[left_index])
            left_index += 1

        elif left_list[left_index] <= right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1

    print(sorted_list)
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


if __name__ == "__main__":
    random_list = random.sample(range(1, 30), 10)
    print(random_list)
    random_list = merge_sort(random_list)
    print(random_list)