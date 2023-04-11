from itertools import chain

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[1] * N for _ in range(N)]
di = [[1, 0], [-1, 0], [0, -1], [0, 1]]

sorted_board = sorted([[board[r][c], r, c] for c in range(N) for r in range(N)])
for _, r, c in sorted_board:
    for i in range(4):
        nr = di[i][0] + r
        nc = di[i][1] + c
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if board[r][c] < board[nr][nc]:
            dp[nr][nc] = max(dp[r][c] + 1, dp[nr][nc])
print(max(chain(*dp)))

"""
커지면서 이동하기 때문에 같은 수 도 안됨.
시작 점을 어떻게 잡지 -> minimum 으로 하기엔, 엣지 케이스도 있을 것 같은데.
"""
