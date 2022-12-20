import sys

input = sys.stdin.readline

N = int(input())
date = []
target = 301
count = 0
end = 0

for _ in range(N):
    a, b, c, d = map(int, input().split())
    date.append([a * 100 + b, c * 100 + d])
date.sort()

while date:
    if target > 1130 or target < date[0][0]:
        break
    for _ in range(len(date)):
        if target >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]
            date.remove(date[0])
        else:
            break
    target = end
    count += 1
if target < 1201:
    print(0)
else:
    print(count)


"""
10 만개를 어케 소팅하노

10
2 15 3 23
4 12 6 5
5 2 5 31
9 14 12 24
6 15 9 3
6 3 6 15
2 28 4 25
6 15 9 27
10 5 12 31
7 14 9 1
"""
