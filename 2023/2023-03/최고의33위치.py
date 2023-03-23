N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
max_v = 0


def square(r, c):
    if r + 2 < N and c + 2 < N:
        return sum(board[r][c:c + 3]) + sum(board[r + 1][c:c + 3]) + sum(board[r + 2][c:c + 3])
    else:
        return 0


if N == 3:
    answer = 0
    for b in board:
        answer += sum(b)
    print(answer)
    exit()
else:
    for r in range(N):
        for c in range(N):
            max_v = max(square(r, c), max_v)
    print(max_v)
