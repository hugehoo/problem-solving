"""
큐 - FIFO

a b c d e

b e d a c


a b c d e

e c a b d
2

"""

from collections import deque

answer = 0
n = int(input())
q1 = deque()

for i in range(n):
    q1.append(input())

for i in range(n):
    out = input()
    if out != q1[0]:
        q1.remove(out)
        answer += 1
    else:
        q1.popleft()

print(answer)
