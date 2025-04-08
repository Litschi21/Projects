import numpy as np
import random
import sys
import time

sys.setrecursionlimit(10_000_001)

def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1
    
    sorted_arr.extend(left[left_idx:])
    sorted_arr.extend(right[right_idx:])

    return sorted_arr

nums = [random.randint(1, 1_000_000_000) for i in range(1, 10_000_001)]

# start = time.time()
# bubble_sort(nums)
# end = time.time()
# bubble_sort_time = end - start

# start = time.time()
# quick_sort(nums)
# end = time.time()
# quick_sort_time = end - start

start = time.time()
merge_sort(nums)
end = time.time()
merge_sort_time = end - start

# print(f'Bubble Sort: {bubble_sort_time} sec')
# print(f'Quick Sort: {quick_sort_time} sec')
print(f'Merge Sort: {merge_sort_time} sec')
