from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            dp[n][m] = board[n - 1][m - 1] + dp[n - 1][m] + dp[n][m - 1] - dp[n - 1][m - 1]
    for _ in range(M):
        row1, col1, row2, col2 = map(int, input().split())
        print(dp[row2][col2] - dp[row1 - 1][col2] - dp[row2][col1 - 1] + dp[row1 - 1][col1 - 1])
"""
결과는 두 문자열의 길이보다 길 수 없다.
가장 긴 최장 부분 수열이 무엇인지 알 필요 없다.
그냥 길이만 알면 됨.

두 문자열은 꼭 같은 길이일 필요 없다.
결과는 가장 짧은 문자열보다 클 수 없다.



"""
