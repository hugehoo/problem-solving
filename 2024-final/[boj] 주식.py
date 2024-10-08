from sys import stdin


def stock(n):
    prices = list(map(int, input().split()))
    highest = prices[-1]
    result = 0
    for i in range(n - 2, -1, -1):
        diff = highest - prices[i]
        if diff > 0:
            result += diff
        else:
            highest = prices[i]
    return result


T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    print(stock(N))

"""
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
"""
