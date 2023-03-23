from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

if M == 1:
    print(2 * N)
else:
    for r_ in range(N):
        queue = deque()
        for idx in range(N):
            if queue:
                if queue[-1] != board[r_][idx]:
                    queue.clear()
                queue.append(board[r_][idx])
            else:
                queue.append(board[r_][idx])
            if len(queue) >= M:
                result += 1
                break
    
    for r_ in range(N):
        col_queue = deque()
        for idx in range(N):
            if col_queue:
                if col_queue[-1] != board[idx][r_]:
                    col_queue.clear()
                col_queue.append(board[idx][r_])
            else:
                col_queue.append(board[idx][r_])
            if len(col_queue) >= M:
                result += 1
                break
    print(result)
