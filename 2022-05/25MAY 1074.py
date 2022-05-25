import sys

input = sys.stdin.readline

N, R, C = map(int, input().split())
board = [[0] * 2 ** N for _ in range(2 ** N)]
start = 1


def recursive(a, b, value):
    print("=> ", [[a, b], [a, b + 1], [a + 1, b], [a + 1, b + 1]])
    for r in [[a, b], [a, b + 1], [a + 1, b], [a + 1, b + 1]]:
        # print("r: ", r, "t: ", t)
        board[r[0]][r[1]] = value
        value += 1
    return value


for n in range(1, N + 1):
    k = 2 ** (n - 1)
    temp = [[0, 0], [0, k], [k, 0], [k, k]]

    for t in temp:
        a, b = t
        # print('t', t, board)
        if board[a][b]:  ## board[0][0] = 0 임 원래...
            continue
        start = recursive(a, b, start)
    for b in board:
        print(b)
    print(' ')
