#!/bin/python3

# Link: https://www.hackerrank.com/challenges/plus-minus/problem
# Difficulty: Easy
# Solution: Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
# Print the decimal value of each fraction on a new line.
#
# Example:
# arr = [1, 1, 0, -1, -1]
# plusMinus(arr)
# Output:
# 0.400000
# 0.400000
# 0.200000

import math
import os
import random
import re
import sys


def plusMinus(arr):
    n = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    # Print the ratios with 6 decimal places
    print("{:.6f}".format(positive_count / n))
    print("{:.6f}".format(negative_count / n))
    print("{:.6f}".format(zero_count / n))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
