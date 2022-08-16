import sys
from collections import deque

input = sys.stdin.readline

""" 1495 """
# N, S, M = map(int, input().split())
# V = list(map(int, input().split()))
#
# dp = [[0] * (M + 1) for _ in range(N + 1)]
# dp[0][S] = 1
#
# for n in range(N):
#     for m in range(M + 1):
#         if dp[n][m]:
#             if m + V[n] <= M:
#                 dp[n+1][m + V[n]] = 1
#             if 0 <= m - V[n]:
#                 dp[n+1][m - V[n]] = 1
#
# for k in range(len(dp[N]) - 1, -1, -1):
#     if dp[N][k]:
#         print(k)
#         exit()
# print(-1)

""" 16928 
dictionary : ladder, snake 저장
주사위 범위 1 ~ 6
이미 방문한 곳은, 결국 제자리 걸음 걷게 되므로 피한다. 
100 은 항상 도달하게 돼 있다.

주사위를 최소 몇번 굴러야하나. 
1 ~ 100 까지의 배열을 만들고, 해당 값에 도달할 때 주사위를 몇번 굴렸는지 저장한다. 
"""

N, M = map(int, input().split())
ladder, snake = {}, {}
visited = [False] * 101
cnt_board = [0] * 101

for _ in range(N):
    i, j = map(int, input().split())
    ladder[i] = j

for _ in range(M):
    i, j = map(int, input().split())
    snake[i] = j


def bfs():
    q = deque([1])
    visited[1] = True
    while q:
        now = q.popleft()
        for dice in range(1, 7):
            now_dice = now + dice
            if now_dice <= 100 and not visited[now_dice]:
                if now_dice in ladder.keys():
                    now_dice = ladder[now_dice]
                elif now_dice in snake.keys():
                    now_dice = snake[now_dice]

                # 이 부분 -> now_dice 가 이미 방문한 곳인지 체크하는 과정을 놓쳤다.
                if not visited[now_dice]:
                    q.append(now_dice)
                    visited[now_dice] = True
                    cnt_board[now_dice] = cnt_board[now] + 1

bfs()
print(cnt_board[100])



print(")|\_/|")
print("|q p|   /}")
print('"( 0 )"""\"')
print("|"^"`    |")
print("||_/=\\__|")