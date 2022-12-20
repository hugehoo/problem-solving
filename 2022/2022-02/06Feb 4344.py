import sys


input = sys.stdin.readline
N = int(input())
for _ in range(N):
    scores = list(map(int, input().split()))
    num, scores = scores[0], scores[1:]
    mean = sum(scores) / num
    above = len(list(filter(lambda x: x > mean, scores)))
    print("{:.3f}%".format(above / num * 100))
