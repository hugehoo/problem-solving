import sys

# def dfs(queen, N, row):
#     count = 0
#
#     if N == row:
#         return 1
#     for col in range(N):
#         queen[row] = col
#
#         for x in range(row):
#             if queen[x] == queen[row]:
#                 break
#             if abs(queen[x] - queen[row]) == (row - x):
#                 break
#         else:
#             count += dfs(queen, N, row + 1)
#     return count
#
#
N = int(sys.stdin.readline())
# queen = [0] * N
#
# answer = dfs(queen, N, 0)
# print(answer)

"""
[권지윤연구원 발표]
onafterrowselection
cleardata() 를 if 문 보다 위로 써줘야한다.
mybatis OR 을 쓰지 않는 이유 => if tag 가 체크해주기 때문이다.

with 절 빼라. 
날짜 필드 (쿼리) 에 문자열 넣지마요, 누난 그새끼 만나지마요.
dt 는 날짜다.
"""


def check(n):
    for i in range(n):
        if (board[n] == board[i]) or (abs(board[n] - board[i]) == (n - i)):
            return False
    return True


def logic(n):
    if n == N:
        global count
        count += 1
    else:
        for i in range(N):
            if visited[i]:
                continue

            board[n] = i  # (n, i) 에 퀸 놓기

            if check(n):  # 퀸 놓을 조건이 맞다면
                visited[i] = True
                logic(n + 1)  # 다음 행으로 넘어간다.
                visited[i] = False


count = 0
board = [0 for _ in range(N)]  # index 번호 = 행, index 값 = 열
visited = [False for _ in range(N)]
logic(0)
print(count)
