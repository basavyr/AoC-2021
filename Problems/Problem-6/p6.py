#!/usr/bin/env python3

import numpy as np

# Problem: [https://adventofcode.com/2021/day/6]

print("Problem 6")

NEW_FISH = 8


INPUT_FILE = "input.dat"

# read the data from the file
with open(INPUT_FILE, 'r+') as f:
    data = f.readline().split(',')

# convert the raw data to integers
original_data = [int(x) for x in data]

data = original_data.copy()


print(data)


def Generate_New_Day(data):
    for id in range(len(data)):
        if data[id] == 0:
            data.append(NEW_FISH)
            data[id] = 6
        else:
            data[id] = data[id] - 1


def Evolve_System(number_of_days, data):
    for day in range(number_of_days):
        Generate_New_Day(data)
    return data


Evolve_System(4,data)

print(data)
