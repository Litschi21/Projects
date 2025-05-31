from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import statistics

puzzles_done = [21, 20, 20, 20, 30, 54, 45, 43, 20, 20, 0, 20, 20, 20, 0, 0, 20, 20, 20, 20, 20] # 1 index = 1 day
plus = [8, 11, 8, 14, 13, 19, 25, 19, 13, 4, 0, 7, 5, 15, 0, 0, 6, 11, 4, 5, 7] # correct without hints
check = [5, 4, 5, 0, 3, 5, 6, 8, 2, 7, 0, 3, 2, 0, 0, 0, 1, 2, 3, 5, 3] # correct with hints
minus = [6, 2, 6, 5, 11, 25, 14, 14, 3, 6, 0, 9, 7, 3, 0, 0, 7, 6, 11, 6, 10] # incorrect without hints
x = [2, 3, 1, 1, 3, 5, 0, 2, 2, 3, 0, 2, 6, 2, 0, 0, 6, 1, 2, 3, 0] # incorrect with hints
ending_rating = [1142, 1223, 1235, 1314, 1321, 1213, 1350, 1311, 1399, 1377, 1377, 1362, 1344, 1442, 1442, 1442, 1430, 1465, 1398, 1364, 1306] # Pr: 1474
days = list(range(1, len(puzzles_done) + 1))

start_date = datetime(2025, 5, 1)
total_days = len(puzzles_done)
dates = [start_date + timedelta(days=i) for i in range(total_days)]

print(f'Days: {len(puzzles_done)}')
print(f'Sum: {sum(puzzles_done)}')
print(f'Median: {round(statistics.median(puzzles_done))}')
print(f'Avg: {round(sum(puzzles_done) / len(puzzles_done), 2)}')

fig, ax = plt.subplots()
ax.plot(days, ending_rating)

ax.grid()
ax.legend(['Puzzle Rating'], loc='upper left')

plt.show()
