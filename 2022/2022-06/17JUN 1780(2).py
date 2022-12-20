import sys

input = sys.stdin.readline


def recursion(N, board, sy, sx):
    if N == 1:
        return board[sy][sx]
    if check(N, board, sy, sx):
        counter[board[sy][sx]] += 1
        return

    nn = N // 3
    for y in range(sy, sy + N, nn):
        for x in range(sx, sx + N, nn):
            recursion(board, N, nn, sy, sx)


def check(board, N, sy, sx):
    val = board[0][0]
    for y in range(sy, sy + N):
        for x in range(sx, sx + N):
            if val != board[y][x]:
                return False
    return True


if __name__ == "__main__":
    counter = {"-1": 0, "0": 0, "1": 0}

    t = int(input())
    entire_board = [list(map(str, input().split())) for _ in range(t)]
    N = len(entire_board[0])
    recursion(N, entire_board, 0, 0)

"""
한변의 길이가 N (3**n) 일 때 3으로 나눴을 때의 몫이, 자르는 기준이 된다.
"""
