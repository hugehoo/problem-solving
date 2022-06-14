# import sys
#
# input = sys.stdin.readline
#
# T, W = map(int, input().split())
# dp = [0] * (T + 1)
# board = [[0, 0] for _ in range(T)]
#
# for t in range(T):
#     n = int(input())
#     board[t][n - 1] = 1
# # board 로 어디에 자두가 떨어질지 알고 있는 상황
# curr = 0
#
# for b in board:
#
#     # 자기 자리에 자두가 떨어지면 그대로 위치 유지
#     # 그렇지 않으면 자리를 옮길수도, 그대로 유지할 수도 있다.
#
#     if b[0] == 1:
#
#         pass
#     else:
#         pass
#
# """
# 7 2
# 2
# 1
# 1
# 2
# 2
# 1
# 1
# """
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T, W = map(int, input().split())
    plums = [0]
    for i in range(T):
        plums.append(int(input()))
    dp = [[0] * (W + 1) for _ in range(T + 1)]
    for i in range(1, T + 1):

        # case 1.
        if plums[i] == 1:
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = dp[i - 1][0]

        # case 2. j 가 1 부터 시작한다는 것은, 최소 한번은 이동을 의미
        for j in range(1, W + 1):
            if j > i:
                break
            previous = max(dp[i - 1][j - 1], dp[i - 1][j])
            if (plums[i] == 1 and j % 2 == 0) or (plums[i] == 2 and j % 2 == 1):
                dp[i][j] = previous + 1
            else:
                dp[i][j] = previous

    print(max(dp[-1]))
