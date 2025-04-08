import matplotlib.pyplot as plt
import numpy as np

numbers = np.array([100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000])
times_single_core = np.array([0.00, 0.01, 0.01, 0.69, 5.34, 34.06, 98.22, 214.92, 412.20, 694.13, 991.04, 1438.92, 2103.15])
times_multi_core_6 = np.array([0.20, 0.20, 0.20, 0.44, 1.70, 9.61, 29.86, 65.80, 127.71, 202.46, 304.12, 447.00, 631.94]) # 100K: 868.30
times_multi_core_12 = np.array([0.26, 0.28, 0.30, 0.57, 1.37, 6.48, 22.37, 47.22, 86.90, 135.93, 210.27, 263.45, 380.01]) # 100K: 505.94
times_multi_core_24 = np.array([0.34, 0.34, 0.32, 0.60, 1.46, 6.09, 17.58, 38.43, 74.99, 122.80, 182.88, 260.1, 368.16])
# times_multi_core_36 = np.array([0.31, 0.50, 0.46, 0.90, 1.88, 6.80, 18.33, 40.46, 73.07, 122.71, 187.18, 274.57, 380.27])

plt.xlabel('Numbers')
plt.ylabel('Time (in sec)')

plt.plot(numbers, times_single_core)
plt.plot(numbers, times_multi_core_6)
plt.plot(numbers, times_multi_core_12)
plt.plot(numbers, times_multi_core_24)
# plt.plot(numbers, times_multi_core_36)

plt.legend(['Single Core', '6 Cores', '12 Cores', '24 Cores'], loc='upper left')
plt.grid()
plt.show()
