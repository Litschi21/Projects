import numpy as np
from pyautogui import write
from random import randint
from time import sleep
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from win32api import mouse_event, SetCursorPos

cell_size = 55
grid_origin_x = 684
grid_origin_y = 248
rand_nums = []
rand_pos_xs = []
rand_pos_ys = []

def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 8, 6, 0, 2, 0, 0],
    [0, 0, 3, 9, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 0, 0, 0, 7, 0],
    [6, 8, 9, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 2, 5],
    [0, 0, 0, 0, 0, 5, 1, 4, 0],
    [9, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 1, 0, 2, 0, 0, 0, 0]
]

grid_copy = [row[:] for row in grid]

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
        if grid[row//3*3 + i//3][col//3*3 + i%3] == num:
            return False
    return True


def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None


def is_done(grid):
    if 0 not in grid:
        return True
    else:
        return False


def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    
    r, c = empty
    
    for num in range(1, 10):
        if is_valid(grid, r, c, num):
            grid[r][c] = num
            if solve(grid):
                return True
            grid[r][c] = 0
    
    return False

solve(grid)
print(np.array(grid))

for r in range(9):
    for c in range(9):
        if grid_copy[r][c] != 0:
            grid_copy[r][c] = 0
        else:
            grid_copy[r][c] = grid[r][c]

for row in range(9):
    for col in range(9):
        num = grid_copy[row][col]
        
        if num == 0:
            continue

        x = grid_origin_x + col * cell_size + cell_size // 2
        y = grid_origin_y + row * cell_size + cell_size // 2

        click(x, y)
        write(str(num), interval=0.02)
