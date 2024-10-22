from sys import stdin

input = stdin.readline


def method_name(board: list, icebergs: list) -> (list, list):
    next_year = [[0] * M for _ in range(N)]
    new_icebergs = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for r, c in icebergs:
        counter = 0
        for i in range(4):
            ny = dy[i] + r
            nx = dx[i] + c
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
                counter += 1
        next_height = board[r][c] - counter
        next_year[r][c] = max(next_height, 0)
        if next_year[r][c] > 0:
            new_icebergs.append([r, c])
    return next_year, new_icebergs


def check_seperate(board, icebergs) -> bool:
    N = len(board)
    M = len(board[0])
    continent = 0
    visited = {}
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for r, c in icebergs:
        if board[r][c] != 0 and visited.get((r, c)) is None:
            stack = [(r, c)]
            visited[(r, c)] = 1
            while stack:
                r_, c_ = stack.pop()
                for i in range(4):
                    ny = dy[i] + r_
                    nx = dx[i] + c_
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != 0 and visited.get((ny, nx)) is None:
                        stack.append([ny, nx])
                        visited[(ny, nx)] = 1
        
            continent += 1
            if continent >= 2:
                return True
    return False


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    icebergs = [(r, c) for r in range(N) for c in range(M) if arr[r][c] > 0]
    
    year = 0
    while True:
        year += 1
        next_board, icebergs = method_name(arr, icebergs)
        result = check_seperate(next_board, icebergs)
        
        for b in next_board:
            if sum(b) != 0:
                break
        else:
            print(0)
            break
            
        if result:
            print(year)
            exit(0)
        arr = next_board

