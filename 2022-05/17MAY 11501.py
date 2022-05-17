import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    while len(arr) >= 2:
        max_idx = arr.index(max(arr))
        semi_total = 0
        for i in arr[:max_idx]:
            semi_total += arr[max_idx] - i
        total += semi_total
        arr = arr[max_idx + 1:]
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
