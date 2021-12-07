#!/usr/bin/env python3

import numpy as np

# Problem: [https://adventofcode.com/2021/day/6]

print("Problem 6")


INPUT_FILE = "input.dat"

# read the data from the file
with open(INPUT_FILE, 'r+') as f:
    data = f.readline().split(',')

# convert the raw data to integers
original_data = [int(x) for x in data]

data = original_data.copy()

data[0] = 1

print(data)
print(original_data)
