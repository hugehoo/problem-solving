N = int(input())
board = [list(map(int, input())) for _ in range(N)]


def dfs(r, c, n):
    check = board[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if check != board[i][j]:
                check = -1
                break
    if check == -1:
        print("(", end='')
        n = n // 2
        dfs(r, c, n)
        dfs(r, c + n, n)
        dfs(r + n, c, n)
        dfs(r + n, c + n, n)
        print(")", end="")
    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")


dfs(0, 0, N)

"""
( (110(0101))(0010)1(0001) )
( 0 (0011) (0(0111)01) 1 )

하나로 나타낼 수 있으면 괄호 필요없다.

"""
