# Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Difficulty: Easy
# Description: Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty. The rating for Alice's challenge is the first element of the list a, and the rating for Bob's challenge is the first element of the list b. Return the comparison points for Alice and Bob.

def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    return [alice_score, bob_score]

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    
    result = compareTriplets(a, b)
    
    print(' '.join(map(str, result)))