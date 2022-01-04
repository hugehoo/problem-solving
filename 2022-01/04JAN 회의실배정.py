from sys import stdin
import heapq

read = stdin.readline

N = int(read())
heap = []
result = []
for _ in range(N):
    a, b = map(int, read().split())
    result.append((a, b))
result = sorted(result, key=lambda x: x[0])
result = sorted(result, key=lambda x: x[1])

count, last = 0, 0
for start, end in result:
    if start >= last:
        count += 1
        last = end
print(count)
