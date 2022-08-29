import sys

input = sys.stdin.readline

N = int(input())

"""
0 -> 1
1 -> 10
배열 2개
  0 1 2 3 4 5 6 7 
A 1 0 1 1 2 3 5 8 13 21 34
B 0 1 1 2 3 5 8 13
"""
arr = [0] * (45 + 1)
arr[1] = 1
arr[2] = 1
for i in range(3, N + 1):
    arr[i] = arr[i - 1] + arr[i - 2]
print(arr[N - 1], arr[N])
# for _ in range(N):
