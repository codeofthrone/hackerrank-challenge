# Link: https://www.hackerrank.com/challenges/sparse-arrays/problem
# Difficulty: Easy
# Description: There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.


def SparseArrays(strings, queries):
    result = []
    for query in queries:
        result.append(strings.count(query))
    return result