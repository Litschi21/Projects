from math import isqrt
from multiprocessing import Pool
from time import time

def prime_num(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    
    return True


nums = list(range(50_000_000))
workers = 12

start = time()

if __name__ == '__main__':
    with Pool(workers) as p:
        results = p.map(prime_num, nums, len(nums) // (workers * 3))

# for num in nums:
#     prime_num(num)

end = time()
print(f'Time taken: {end - start:.2f} seconds')

# 6 Cores
# 100k: 0.23 sec
# 500k: 0.42 sec
# 1 mio: 0.78 sec
# 5 mio: 5.88 sec
# 10 mio: 15.56 sec
# 20 mio: 40.97 sec
# 30 mio: 72.74 sec
# 40 mio: 119.85 sec
# 50 mio: 159.49 sec

# 12 Cores
# 100k: 0.31 sec
# 500k: 0.5 sec
# 1 mio: 0.85 sec
# 5 mio: 4.28 sec
# 10 mio: 11.19 sec
# 20 mio: 30 sec
# 30 mio: 52.84 sec
# 40 mio: 87.86 sec
# 50 mio: 114.54 sec

# Diff (for 12 Core)
# 100k: +0.09 sec
# 500k: +0.08 sec
# 1 mio: +0.07 sec
# 5 mio: -1.6 sec
# 10 mio: -4.37 sec
# 20 mio: -10.97 sec
# 30 mio: -19.9 sec
# 40 mio: -31.99 sec
# 50 mio: -44.95 sec
