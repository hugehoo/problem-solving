import sys

input = sys.stdin.readline

N = int(input())
before = [int(input()) for _ in range(N)]
after = []
count = 0
for i in range(len(before)):
    while after and after[-1] <= before[i]:
        after.pop()
    count += len(after)
    after.append(before[i])

print(count)

"""

10000 * 10000
 
6
10
3
7
4
12
2

6
12
5
7
4
8
1
"""
