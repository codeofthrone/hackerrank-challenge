# Link: https://www.hackerrank.com/challenges/lonely-integer/problem
# Difficulty: Easy
# Solution: Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    for num in a:
        if a.count(num) == 1:
            return num