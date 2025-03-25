def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split()))
    result = aVeryBigSum(ar)
    print(result)