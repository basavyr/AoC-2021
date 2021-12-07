#!/usr/bin/env python3

# Problem: [https://adventofcode.com/2021/day/6]

print("Problem 6")


INPUT_FILE = "input.dat"

# read the data from the file
with open(INPUT_FILE, 'r+') as f:
    data = f.readline().split(',')

# convert the raw data to integers
data = [int(x) for x in data]

print(data)
