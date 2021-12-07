#!/usr/bin/env python3

import numpy as np

# Problem: [https://adventofcode.com/2021/day/6]

print("Problem 6")

# value of a newly born lantern fish, from a zero (0) valued lantern
NEW_FISH = 8
# number of days to perform the evolution of the entire system of lanterns
NUMBER_OF_DAYS = 18
# value to be attributed to a lantern that reaches its expiration date -> 0
RESET_FISH = 6

# name of the input file with the initial lantern setup
INPUT_FILE = "input.dat"

# read the data from the file
with open(INPUT_FILE, 'r+') as f:
    data = f.readline().split(',')

# convert the raw data to integers
original_data = [int(x) for x in data]

# shallow copy for the initial data to perform calculations, keeping the original data intact
data = original_data.copy()


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


def Test_Evolution(tests, NUMBER_OF_DAYS):
    for day in range(1, NUMBER_OF_DAYS + 1):
        data = original_data.copy()
        Evolve_System(day, data)
        print(data)
        if(data == tests[day - 1]):
            print('day', day, '-> all good')
        data.clear()


Test_Evolution(tests, NUMBER_OF_DAYS)
