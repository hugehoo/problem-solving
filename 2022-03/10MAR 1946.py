import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    temp = []
    for _ in range(int(input())):  # 100_000
        a, b = map(int, input().split())
        temp.append((a, b))
    temp.sort(reverse=True)
    count = 0
    # print(temp)
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):

            if temp[i][1] == 1:
                break
            if temp[i][1] > temp[j][1]:
                # print('i', i, ' j ', j)
                # print(temp[i][1], temp[j][1])
                count += 1
                break
    print(len(temp) - count)
"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""
