from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    cards = [0] + list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for k in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - k] + cards[k])
    print(dp[N])
"""
결과는 두 문자열의 길이보다 길 수 없다.
가장 긴 최장 부분 수열이 무엇인지 알 필요 없다.
그냥 길이만 알면 됨.

두 문자열은 꼭 같은 길이일 필요 없다.
결과는 가장 짧은 문자열보다 클 수 없다.



"""
