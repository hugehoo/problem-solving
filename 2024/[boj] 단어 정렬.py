import sys

input = sys.stdin.readline
arr = list(set([input().strip() for _ in range(int(input()))]))
arr.sort(key=lambda x: (len(x), x))
for a in arr:
    print(a)

"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""
