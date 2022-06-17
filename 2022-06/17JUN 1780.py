import sys
from collections import Counter
from itertools import chain

input = sys.stdin.readline


def check(board):
    set_ = set()
    n = board[0][0]
    if len(board[0]) == 1:
        return board[0][0]

    for i in chain(*board):
        set_.add(i)
    if len(set_) == 1:
        return n
    else:
        return False


def divide(board, N):
    mok = N // 3
    for i in range(3):

        for j in range(3):
            temp_ent = []
            for row in board[mok * i: mok * (i + 1)]:
                temp_ent.append(row[mok * j: mok * (j + 1)])
            if check(temp_ent) != False:
                counter.append(check(temp_ent))
            else:
                divide(temp_ent, len(temp_ent[0]))

    return Counter(counter)


if __name__ == "__main__":
    counter = []
    t = int(input())
    entire_board = [list(map(str, input().split())) for _ in range(t)]
    N = len(entire_board[0])
    answer = divide(entire_board, N)
    print(answer['-1'])
    print(answer['0'])
    print(answer['1'])

"""
한변의 길이가 N (3**n) 일 때 3으로 나눴을 때의 몫이, 자르는 기준이 된다.
"""