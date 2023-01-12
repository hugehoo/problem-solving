N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]


def flip(R, C):
    for r in range(R + 1):
        for c in range(C + 1):
            # 방법 1
            board[r][c] = 0 if board[r][c] else 1

            # 방법 2
            board[r][c] ^= 1

            # 방법 1, 2 중 하나를 주석 처리해서 사용


count = 0
for n in range(N - 1, -1, -1):
    for m in range(M - 1, -1, -1):
        if board[n][m]:
            count += 1
            flip(n, m)

print(count)

"""
2 2
00
01


3 3 
101
110
000

011
000
000

100
000
000

000
000
000

"""
