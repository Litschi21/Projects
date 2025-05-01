from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import statistics

puzzles_done = [20]
plus = [7]
check = [5]
x = [2]
minus = [6]
days = list(range(1, len(puzzles_done) + 1))

start_date = datetime(2025, 4, 30)
total_days = len(puzzles_done)
dates = [start_date + timedelta(days=i) for i in range(total_days)]

print(f'Days: {len(puzzles_done)}')
print(f'Sum: {sum(puzzles_done)}')
print(f'Median: {round(statistics.median(puzzles_done))}')
print(f'Avg: {round(sum(puzzles_done) / len(puzzles_done), 2)}')

plt.figure().set_figwidth(22)
plt.plot(days, puzzles_done)
plt.plot(days, plus)
plt.plot(days, minus)

plt.grid()
plt.xlabel('Days')
plt.ylabel('Puzzles Done')
plt.title('Puzzles Done Over Time')
plt.legend(['Puzzles Done', 'Plus', 'Check', 'X', 'Minus'])

plt.show()
