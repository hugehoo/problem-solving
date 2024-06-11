import sys

input = sys.stdin.readline

board_dict = {}
board = []


def check_board(checks: list):
    count = 0
    # 왼쪽 대각선 체크
    if [0, 0] in checks and [1, 1] in checks and [2, 2] in checks and [3, 3] in checks and [4, 4] in checks:
        count += 1
    # 오른쪽 대각선 체크
    if [0, 4] in checks and [1, 3] in checks and [2, 2] in checks and [3, 1] in checks and [4, 0] in checks:
        count += 1
    
    # 각 행렬 체크
    for i in range(5):
        if [i, 0] in checks and [i, 1] in checks and [i, 2] in checks and [i, 3] in checks and [i, 4] in checks:
            count += 1
        
        if [0, i] in checks and [1, i] in checks and [2, i] in checks and [3, i] in checks and [4, i] in checks:
            count += 1
    
    return count >= 3


# 보드판 생성
for i in range(5):
    for j, n in enumerate(list(map(int, input().split()))):
        board_dict[n] = [i, j]

# 사회자가 부르는 순서 -> seq 에 저장
for i in range(5):
    for j, s in enumerate(list(map(int, input().split()))):
        board.append([board_dict[s][0], board_dict[s][1]])
        answer = i * 5 + j + 1
        if answer >= 11 and check_board(board):
            print(answer)
            exit(0)
