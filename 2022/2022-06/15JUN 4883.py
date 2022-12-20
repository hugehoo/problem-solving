import sys
from copy import deepcopy

input = sys.stdin.readline

if __name__ == "__main__":
    case = 0

    while True:
        N = int(input())
        case += 1
        if N == 0:
            exit()
        board = [list(map(int, input().split())) for _ in range(N)]

        # 초기 dp 세팅
        dp = [[0] * 3 for _ in range(N)]
        dp[1][0] = board[1][0] + board[0][1]
        dp[1][1] = board[1][1] + min(dp[1][0], board[0][1], board[0][1] + board[0][2])  # dp[1][0] 있고 없고의 차이
        dp[1][2] = board[1][2] + min(board[0][1], board[0][1] + board[0][2], dp[1][1])
        for i in range(2, N):
            for c in range(3):
                if c == 0:
                    min_v = min(dp[i - 1][0], dp[i - 1][1])
                elif c == 1:
                    min_v = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0])
                else:
                    min_v = min(dp[i - 1][2], dp[i - 1][1], dp[i][1])
                dp[i][c] = board[i][c] + min_v
        print("%d. %d" % (case, dp[-1][1]))
"""
다음 행이 모두 같은 수일 땐, 어디로 가야하나. 
dp 배열을 모두 업뎃 시키면 된다. 업뎃 시킨 배열에 curr-index 가 모두 존재할 수 있다. 업뎃시킨 위치에서 또 일일이 다음행의 최소 자리를 찾고 옮기면 된다. 
dp 배열을 그냥 board 랑 똑같이 만드러놓고 비교할까?
비용 : -1000 < cost < 1000

4
13 7 5
7 13 6
14 3 12
15 6 16
0

4
13 -7 5
7 13 6
14 3 12
15 6 16
0

3
1 1 1
1 1 1
-1 1 1
0
"""
