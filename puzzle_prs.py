import matplotlib.pyplot as plt

sudoku_easy = [217] # in sec
sudoku_medium = [209] # in sec
sudoku_hard = [226] # in sec
sudoku_expert = [265, 255] # in sec
sudoku_master = [314] # in sec
sudoku_extreme = [1154] # in sec

ny_times_sudoku_easy = [292, 251] # in sec
ny_times_sudoku_medium = [1293] # in sec
ny_times_sudoku_hard = [] # in sec

timeguessr_daily = [37994] # points
timeguessr_normal = [40833] # points

seterra_europe = [70, 69, 67, 65, 64, 50, 47.740, 46.528, 45.224] # in sec
seterra_us_states = [77.879, 75.102] # in sec
seterra_asia = [80.401, 75.339] # in sec

time = list(range(len(seterra_europe)))

plt.plot(time, seterra_europe)
plt.grid()
plt.show()