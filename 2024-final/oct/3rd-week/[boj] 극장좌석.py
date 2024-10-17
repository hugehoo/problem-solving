import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    m = int(input().rstrip())
    
    vips = [int(input().rstrip()) for _ in range(m)]
    
    dp = [0] * (n + 1)
    
    # 1~3단계 값 초기화
    dp[0] = 1
    dp[1] = 1
    
    # dp 돌리기
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    answer = 1
    if m >= 1:
        tmp = 0
        for i in range(m):
            answer *= dp[vips[i] - 1 - tmp]
            tmp = vips[i]
        answer *= dp[n - tmp]
    else:
        answer = dp[n]
    print(answer)