# Link: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Difficulty: Easy
# Solution: Given an array of integers, find the number of pairs of integers whose sum is divisible by k.
# Enter your code here. Read input from STDIN. Print output to STDOUT

def divisibleSumPairs(n, k, ar):
    count = 0
    # Remainder frequency array
    remainder_count = [0] * k
    
    # Traverse the array and count remainders
    for num in ar:
        remainder = num % k
        complement = (k - remainder) % k  # The remainder that would make the sum divisible by k
        count += remainder_count[complement]  # Count how many previous numbers have the complement remainder
        remainder_count[remainder] += 1  # Increment the count for this remainder
    
    return count