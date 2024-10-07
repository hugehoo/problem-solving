import sys

from collections import defaultdict

input = sys.stdin.readline
N = int(input())
line = int(input())
temp = defaultdict(list)
for _ in range(line):
    n1, n2 = list(map(int, input().split()))
    temp[n1].append(n2)
    temp[n2].append(n1)

already = set()
values = temp[1]
for v in values:
    already.add(v)
for a in already:
    temp_values = temp[a]
    for t in temp_values:
        if t not in already:
            already.add(t)
print(already)

"""
dictionary 로 리스트 추가

어케할까.

"""
