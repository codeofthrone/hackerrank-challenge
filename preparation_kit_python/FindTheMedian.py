# Link: https://www.hackerrank.com/challenges/find-the-median/problem
# Difficulty: Easy
# Description: The median of a list of numbers is essentially its middle element after sorting. The same number of elements occur after it as before. Given a list of numbers with an odd number of elements, can you find the median?


def findMedian(arr):
    arr.sort()
    
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[(n // 2) - 1] + arr[n // 2]) / 2


