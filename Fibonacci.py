def fibonaccying(func):
    def wrapper(*args, **kwargs):
        print('Fibonaccying...')
        func(*args, **kwargs)
    return wrapper

@fibonaccying
def fibonacci(amt):
    nums = [0, 1]

    for i in range(0, amt):
        nums.append(nums[i] + nums[i + 1])
        print(nums[-1])
    
    print(nums)
    return nums


fibonacci(10_000)
