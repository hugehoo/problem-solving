import sys
from itertools import chain

input = sys.stdin.readline


def check(board):
    set_ = set()
    n = board[0][0]
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
                answer.append(check(temp_ent))
            # else:
            #     divide(temp_ent, len(temp_ent[0]))

    print(answer)
        # for row in board[mok * i: mok * (i + 1)]:
        #     print("row ", row)
        #     for j in range(3):
        #         print("split row ", row[mok * j: mok * (j + 1)])
        #         temp_ent.append(row[mok * j: mok * (j + 1)])
        #     print(check(temp_ent))
        # for j in range(3):
        #     board[mok * i][mok * j]

    # [mok * 0  : mok * 1] [mok * 0  : mok * 1], [mok * 1  : mok * 2], [mok * 2  : mok * 3]
    # [mok * 1  : mok * 2]
    # [mok * 2  : mok * 3]
    return


if __name__ == "__main__":
    answer = []
    t = int(input())  # 3 9 27 81
    entire_board = [list(map(str, input().split())) for _ in range(t)]
    N = len(entire_board[0])
    divide(entire_board, N)
    # for e in entire_board[0:3]:
    #     print(e[0:3])

"""
한변의 길이가 N (3**n) 일 때 3으로 나눴을 때의 몫이, 자르는 기준이 된다. 
"""
