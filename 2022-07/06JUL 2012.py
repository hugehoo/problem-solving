import sys
input = sys.stdin.readline

print(sum([abs((idx + 1) - value) for idx, value in enumerate(sorted([int(input()) for _ in range(1, int(input()) + 1)]))]))






"""
5
1
5
3
1
2
"""