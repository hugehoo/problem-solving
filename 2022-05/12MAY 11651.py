import sys

input = sys.stdin.readline

n = int(input())
coord = [list(map(int, input().split())) for _ in range(n)]
result = sorted(coord, key=lambda x: (x[1], x[0]))
for r in result:
    print(*r)

"""
어떻게 wbwb 를 체크할지
"""
