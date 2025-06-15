import numpy as np
from PIL import Image
from pyautogui import write
import pytesseract
from random import randint
from time import sleep
from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from win32api import mouse_event, SetCursorPos

pytesseract.pytesseract.tesseract_cmd = r"E:\Desk\Pytesseract\tesseract.exe"

cell_size = 55
grid_origin_x = 816
grid_origin_y = 259
rand_nums = []
rand_pos_xs = []
rand_pos_ys = []

grid_region = [790, 233, 55, 55]

def click(x, y):
    SetCursorPos((x, y))
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

grid1 = []
grid2 = []
grid3 = []
grid4 = []
grid5 = []
grid6 = []
grid7 = []
grid8 = []
grid9 = []

grid = [
    grid1,
    grid2,
    grid3,
    grid4,
    grid5,
    grid6,
    grid7,
    grid8,
    grid9
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

def read_sudoku(grid_region):
    for i in range(9):
        for j in range(9):
            screenshot = screenshot(region=grid_region)
            screenshot.save("images/sudoku.png")

            img = Image.open()
            output = pytesseract.image_to_string(img)
            grid str(i).append(output)
            
            grid_region = [x+55 for x in grid_region]

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

        x = grid_origin_x + col * cell_size
        y = grid_origin_y + row * cell_size

        click(x, y)
        write(str(num), interval=0.02)
