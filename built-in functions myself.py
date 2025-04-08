import random

def total_sum(num_list):
    complete_sum = 0

    for num in num_list:
        complete_sum += num

    return complete_sum

def minimum(num_list):
    lowest = num_list[0]

    for num in num_list:
        if num < lowest:
            lowest = num

    return lowest

def maximum(num_list):
    highest = num_list[0]

    for num in num_list:
        if num > highest:
            highest = num

    return highest

def sort(num_list):
    sorted_list = []
    lowest = num_list[0]

    while num_list:
        lowest = num_list[0]

        for num in num_list:
            if num < lowest:
                lowest = num

        sorted_list.append(lowest)
        num_list.remove(lowest)

    return sorted_list


nums = [random.randint(0, 10_000) for i in range(1000)]
print(total_sum(nums))
print(minimum(nums))
print(maximum(nums))
print(sort(nums))
