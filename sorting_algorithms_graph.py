import matplotlib.pyplot as plt

num_amt = [10_000, 100_000, 1_000_000, 10_000_000]
tim_sort = [0, 0.02, 0.27, 4.53]
merge_sort = [0.03, 0.47, 5.55, 68.13]

plt.plot(num_amt, tim_sort, label='Tim Sort')
plt.plot(num_amt, merge_sort, label='Merge Sort')
plt.grid()

plt.xlabel('Nums')
plt.ylabel('Sec')
plt.legend(loc='upper left')
plt.show()
