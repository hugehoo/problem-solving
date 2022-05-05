import sys

input = sys.stdin.readline

first = list(input().strip())
second = list(input().strip())
third = list(input().strip())


def compare(first_, second_):
    first_ = [0] + first_
    second_ = [0] + second_
    board = [[0] * (len(first_)) for _ in range(len(second_))]

    for sec in range(1, len(second_)):
        for fir in range(1, len(first_)):
            if first_[fir] == second_[sec]:
                board[sec][fir] += (board[sec - 1][fir - 1] + 1)
            else:
                board[sec][fir] = max(board[sec - 1][fir], board[sec][fir - 1])

    r = len(second_) - 1
    c = len(first_) - 1

    result = []
    while True:
        if board[r][c] == 0:
            break
        if board[r][c] != board[r - 1][c] and board[r][c] != board[r][c - 1]:
            result.append(first_[c])
            r -= 1
            c -= 1
            continue

        if board[r][c] == board[r - 1][c]:
            r -= 1
            continue
        if board[r][c] == board[r][c - 1]:
            c -= 1
            continue
    return ''.join(result[::-1])


middle = compare(first, second)
answer = compare(list(middle), third)
print(len(answer))

