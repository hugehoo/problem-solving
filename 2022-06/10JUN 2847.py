import sys

input = sys.stdin.readline

N = int(input())

board = [int(input()) for _ in range(N)]
board = board[::-1]
max_v = board[0]
answer = 0
for i in range(1, len(board)):
    if max_v - board[i] > 0:
        # diff = max_v - board[i]
        # answer += diff
        # max_v = board[i] - diff
        max_v = board[i]
        # print('1 ')
        continue
    elif max_v - board[i] < 0:
        diff = max_v - board[i]
        answer += abs(diff - 1)
        max_v = board[i] + (diff - 1)
        # print('2 ', answer, max_v, board[i])

    else:
        answer += 1
        max_v = board[i - 1] - 1
        # print('3 ', answer, max_v, board[i])

print(answer)

"""
내림차순으로 만들어야함. 
항상 답이 있는 경우만 존재. 

3
5
5
5
"""
