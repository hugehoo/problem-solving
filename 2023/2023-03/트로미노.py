R, C = map(int, (input().split()))
board = [list(map(int, input().split())) for i in range(R)]
max_value = 0


def find(r, c):
    global max_value
    v1, v2, v3, v4, v5, v6 = 0, 0, 0, 0, 0, 0
    
    try:
        v1 = board[r][c] + board[r][c + 1] + board[r][c + 2]
    except IndexError:
        pass
    
    try:
        v2 = board[r][c] + board[r + 1][c] + board[r + 2][c]
    except IndexError:
        pass
    
    try:
        v3 = board[r][c] + board[r][c + 1] + board[r + 1][c]
    except IndexError:
        pass
    
    try:
        v4 = board[r][c] + board[r][c + 1] + board[r - 1][c]
    except IndexError:
        pass
    
    try:
        v5 = board[r][c] + board[r][c - 1] + board[r + 1][c]
    except IndexError:
        pass
    
    try:
        v6 = board[r][c] + board[r][c - 1] + board[r - 1][c]
    except IndexError:
        pass
    
    return max(max_value, v1, v2, v3, v4, v5, v6)


for r in range(R):
    for c in range(C):
        max_value = find(r, c)
print(max_value)

"""
R, C <= 200 이기 때문에, 이중 for 문 돌아도 N = 40000.
완전탐색으로 접근해도 괜찮다고 판단할 수 있다.

3 3
1 2 3
3 2 1
3 1 1
>> 8

4 5
6 5 4 3 1
3 4 4 14 1
6 1 3 15 5
3 5 1 16 3
>> 45
"""
