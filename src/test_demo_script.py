#!/usr/bin/env python3

'''
    Simple program to find the solution to a quadratic
    equation using python3
    Also, added some pytest unit-test functions
'''

import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def testsquare():
    num = 7
    assert (num ** 2) == 40
