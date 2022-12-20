from sys import stdin

n = int(stdin.readline())

stairs = [[0] * 10 for _ in range(n + 1)]

# 초기값 설정
stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    # 계단 수가 0으로 끝나는 경우
    stairs[i][0] = stairs[i - 1][1]
    # 계단 수가 9로 끝나는 경우
    stairs[i][9] = stairs[i - 1][8]

    # 계단 수가 1~8로 끝나는 경우
    for j in range(1, 9):
        stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]
for s in stairs:
    print(s)
print(sum(stairs[n]) % 1000000000)

N = int(input())
array = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
board = []
if N == 1:
    print(9)
    exit()
else:
    board.append(array)
    for n in range(1, N):
        temp = []
        for j in range(10):
            if j == 0:
                temp.append((board[n - 1][1]))
            elif j == 9:
                temp.append((board[n - 1][8]))
            else:
                temp.append((board[n - 1][j - 1] + board[n - 1][j + 1]))
        board.append(temp)
print(sum(board[-1]) % 1000000000)
"""
1<= N <= 100
1개일 때 : 9
2개일 때: 17
3개일 때 : 32
4개일 때 : 62
"""
