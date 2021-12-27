import sys


read = sys.stdin.readline
N = int(read())
RGB = [list(map(int, read().split())) for _ in range(N)]

for i in range(1, N):
    RGB[i][0] += min(RGB[i - 1][1], RGB[i - 1][2])
    RGB[i][1] += min(RGB[i - 1][0], RGB[i - 1][2])
    RGB[i][2] += min(RGB[i - 1][1], RGB[i - 1][0])
print(min(RGB[N - 1]))


"""
3
26 40 83
49 60 57
13 89 99

3
1 100 100
100 100 100
1 100 100
"""
