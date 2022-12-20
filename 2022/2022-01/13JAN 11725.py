import sys
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(start, tree, result):
    for a in tree[start]:
        if result[a] == 0:
            result[a] = start
            dfs(a, tree, result)


dfs(1, tree, result)
for r in result[2:]:
    print(r)

"""
7
1 6
6 3
3 5
4 1
2 4
4 7


12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

"""
