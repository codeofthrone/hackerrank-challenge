#!/bin/python3

# Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Difficulty: Easy
# Solution : Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
# For example, assume her scores for the season are represented in the array scores = [12, 24, 10, 24]. Scores are in the same order as the games played. She would tabulate her results as follows:
# Game  Score  Minimum  Maximum  Min Breaks  Max Breaks

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    if not scores:
        return [0,0]
    
    min_score, max_score = scores[0], scores[0]
    min_break, max_break = 0, 0
    
    for i in scores:
        if i > max_score:
            max_score = i
            max_break += 1
        if i < min_score:
            min_score = i
            min_break += 1
    return [max_break, min_break]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
