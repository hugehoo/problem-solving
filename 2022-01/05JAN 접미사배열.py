from sys import stdin

N = stdin.readline().strip()
for r in sorted([N[i:] for i in range(len(N))]):
    print(r)

"""
baekjoon
"""
