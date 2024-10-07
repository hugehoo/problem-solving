import sys

input = sys.stdin.readline
N, K = map(int, input().split())
# 지목 여부
choice = [False] * N
choice[0] = True

numbers = [int(input()) for _ in range(N)]

i = 0
for r in range(N):
    M = numbers[i]
    if M == K:
        print(r + 1)
        break

    if choice[M]:  # 지목한 사람이 중복시 -1 출력
        print(-1)
        break
    choice[M] = True
    i = M
