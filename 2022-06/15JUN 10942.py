import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    dp = [[0] * N for _ in range(N)]

    for num in range(N):
        for start in range(N - num):
            end = start + num

            if start == end:
                dp[start][end] = 1
            elif arr[start] == arr[end]:
                if (start + 1 == end) or (dp[start + 1][end - 1] == 1):
                    dp[start][end] = 1

    for _ in range(M):
        a, b = map(int, input().split())
        print(dp[a - 1][b - 1])

