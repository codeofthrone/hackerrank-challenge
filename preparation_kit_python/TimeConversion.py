#!/bin/python3

#Link: https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty: Easy
# Solution: Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:].upper()
    time_string = s[:-2]
    hh, mm, ss = time_string.split(':')
    hh = int(hh)
    if period == "PM" and hh != 12:
        hh += 12
    elif period == "AM" and hh ==12:
        hh = 0
    return "{:02d}:{}:{}".format(hh,mm,ss)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
