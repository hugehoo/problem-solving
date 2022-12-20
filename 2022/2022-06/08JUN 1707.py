import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
M = 0
p, t = [], []
dp = [0] * (N + 1)

RED = 1


def bfs(idx, color):
    q = deque()
    q.append(idx)

    global checkBigraph
    colors[idx] = color
    while q and checkBigraph:
        p = q.popleft()
        for k in list_dict[p]:
            if not colors[k]:
                q.append(k)
                colors[k] = colors[p] * -1
            elif colors[k] + colors[p] != 0:
                checkBigraph = False
                return


for _ in range(N):
    v, e = map(int, input().split())
    colors = [0] * (v + 1)
    list_dict = defaultdict(list)
    checkBigraph = True

    for _ in range(e):
        a, b = map(int, input().split())
        list_dict[a].append(b)
        list_dict[b].append(a)

    for i in range(1, v + 1):
        if not colors[i]:
            bfs(i, RED)
    print("YES" if checkBigraph else "NO")

