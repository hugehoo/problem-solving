import sys

input = sys.stdin.readline
arr = []
result = []
N = int(input())
for _ in range(N):
    name, day, month, year = map(str, input().split())
    result.append((arr[0], int(arr[3]), int(arr[2]), int(arr[1])))
    
result.sort(key=lambda x: (x[1], x[2], x[3]))
print(result[N - 1][0])
print(result[0][0])



