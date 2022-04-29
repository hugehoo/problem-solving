import sys
import math

input = sys.stdin.readline

eratos = [1] * (2 * 123456 + 1)
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = 0
while True:
    n = int(input())
    if n == 0:
        break

    doubled = 2 * n

    answer = sum(eratos[n + 1: doubled + 1])
    print(answer)

"""
100,000
10만 1 -> 20만
200,000
"""
