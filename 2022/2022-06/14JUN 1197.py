import sys

input = sys.stdin.readline

V, E = map(int, input().split())
parent = [0] * (V + 1)

for i in range(1, (V + 1)):
    parent[i] = i

answer = 0


def union_parent(parents, a, b, c):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    global answer
    if a != b:
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
        answer += c


def find_parents(parents, x):
    if parents[x] != x:
        return find_parents(parents, parents[x])
    return parents[x]


board = [list(map(int, input().split())) for _ in range(E)]
board = sorted(board, key=lambda x: x[2])
for a, b, c, in board:
    union_parent(parent, a, b, c)
print(answer)

"""
3 3
2 3 2
1 3 3
1 2 1

5 5
1 3 2
1 5 1
2 4 3
2 3 5
3 4 4


6 9
1 6 10
3 4 12
2 7 15
2 3 16
4 7 18
4 5 22
5 7 25
5 6 27
1 2 29
"""
