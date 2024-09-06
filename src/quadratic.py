#!/usr/bin/env python3

'''
    Simple program to find the solution to a quadratic
    equation using python3
'''

import cmath

# Variable declarations
a = 1
b = 5
c = 6

# Calculate the discriminant
d = (b ** 2) - (4 * a * c)

# Find solutions
sol1 = (-b - cmath.sqrt(d) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

# Finally, print the result
print(f"sol1: {sol1}, sol2: {sol2"
