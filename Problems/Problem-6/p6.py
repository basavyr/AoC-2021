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


# print(data)


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


def Read_Test_Input(test_file):
    proper_lines = []
    with open(test_file, 'r+') as f:
        lines = f.readlines()
    for line in lines:
        line = [int(x) for x in line.strip().split(',')]
        proper_lines.append(line)
    return proper_lines


tests = Read_Test_Input('tests.dat')
print(tests[0])

# Evolve_System(1, data)

# print(data)
