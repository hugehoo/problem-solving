def solution(N, board):
    matrix = [board[N * (i - 1): N * i] for i in range(1, len(board) // N + 1)]
    center = N // 2
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    dp = [[float('inf')] * N for _ in range(N)]
    dp[center][center] = matrix[center][center]
    for y in range(center, -1, -1):
        for x in range(center, -1, -1):
            search(N, center, directions, dp, matrix, x, y)

    for y in range(center, -1, -1):
        for x in range(center, N):
            search(N, center, directions, dp, matrix, x, y)

    for y in range(center, N):
        for x in range(center, -1, -1):
            search(N, center, directions, dp, matrix, x, y)

    for y in range(center, N):
        for x in range(center, N):
            search(N, center, directions, dp, matrix, x, y)

    compare = [dp[i][0] for i in range(N)]
    compare.extend([dp[i][-1] for i in range(N)])
    compare.extend(dp[0])
    compare.extend(dp[-1])
    # compare = []
    # for d in dp:
    #     compare.append(d[0])
    #     compare.append(d[-1])
    # compare += dp[0]
    # compare += dp[-1]
    return min(compare)


def search(N, center, directions, dp, matrix, x, y):
    for i in range(4):
        ny = y + directions[i][0]
        nx = x + directions[i][1]
        if max(abs(x - center), abs(y - center)) > max(abs(nx - center),
                                                       abs(ny - center)) or ny == nx or (
                ny >= N or ny < 0 or nx >= N or nx < 0):
            continue
        dp[ny][nx] = min(matrix[ny][nx] + dp[y][x], dp[ny][nx])


print(solution(5, [9, 3, 9, 9, 9,
                   5, 2, 7, 8, 9,
                   8, 1, 5, 8, 9,
                   6, 1, 8, 7, 9,
                   9, 9, 8, 9, 9]))

print(solution(6, [9, 3, 9, 9, 9, 1, 2,
                   5, 2, 7, 8, 9, 1, 2,
                   8, 1, 5, 8, 9, 1, 2,
                   6, 1, 8, 7, 9, 1, 2,
                   6, 1, 8, 7, 9, 1, 2,
                   9, 9, 8, 9, 9, 1, 2,
                   6, 1, 8, 7, 9, 1, 2
                   ]))

"""

"""
