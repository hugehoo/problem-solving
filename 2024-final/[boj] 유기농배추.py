import sys
from collections import deque

input = sys.stdin.readline

direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    result = 0
    # 0. board 완성
    board = [[0 for _ in range(M)] for _ in range(N)]
    check = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        board[r][c] = 1
    
    # 1. 배추 찾기
    stack = deque()
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and check[y][x] != 1:
                check[y][x] = 1
                stack.append([y, x])
                result += 1
                while stack:
                    ny, nx = stack.popleft()
                    for i in range(4):
                        dy = direction[i][0] + ny
                        dx = direction[i][1] + nx
                        if 0 <= dy < N and 0 <= dx < M and check[dy][dx] != 1 and board[dy][dx] == 1:
                            stack.append([dy, dx])
                            check[dy][dx] = 1
    print(result)

"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

"""
