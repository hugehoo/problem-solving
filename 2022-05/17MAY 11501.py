import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    max_value = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] > max_value:
            max_value = arr[i]
        else:
            total += (max_value - arr[i])
    print(total)

"""
1
3
3 5 9

3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
"""
