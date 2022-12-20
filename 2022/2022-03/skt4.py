from itertools import permutations


def solution(n, edges):
    board = [[float('inf')] * n for _ in range(n)]
    for a, b in edges:
        board[a][b] = 1
        board[b][a] = 1

    for k in range(n):
        for s in range(n):
            for e in range(n):
                if s != e:
                    board[s][e] = min(board[s][e], board[s][k] + board[k][e])

    count = 0
    arr = [i for i in range(n)]
    for i, j, k in permutations(arr, 3):
        if board[i][k] == board[i][j] + board[j][k]:
            count += 1

    return count


solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
solution(4, [[2, 3], [0, 1], [1, 2]])
