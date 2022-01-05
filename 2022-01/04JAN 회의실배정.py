from sys import stdin


read = stdin.readline

heap = []
result = []
N = int(read())

for _ in range(N):
    a, b = map(int, read().split())
    result.append((a, b))
# result = sorted(result, key=lambda x: x[0])
result = sorted(result, key=lambda x: x[1])
count, last = 0, 0
for start, end in result:
    if start >= last:
        count += 1
        last = end
print(count)

#  [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]