result = set()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = [list(map(str, input().split())) for _ in range(5)]


def dfs(r_, c_, tmp):
    if len(tmp) == 6:
        result.add(tmp)
        return

    for i in range(4):
        nx = c_ + dx[i]
        ny = r_ + dy[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            dfs(ny, nx, tmp + res[ny][nx])


for r in range(5):
    for c in range(5):
        dfs(r, c, res[r][c])
print(len(result))

# recursion exceeded
# def dfs(r_, c_, tmp):
#     if len(tmp) == 6:
#         result.add(''.join(map(str, tmp)))
#         return
#
#     for i in range(4):
#         nx = c_ + dx[i]
#         ny = r_ + dy[i]
#         if 0 <= ny < 5 and 0 <= nx < 5:
#             tmp.append(res[ny][nx])
#             dfs(ny, nx, tmp)
#
#
# for r in range(5):
#     for c in range(5):
#         temp = [res[r][c]]
#         dfs(r, c, temp)
# print(result)

"""
이중 포문 돌면서, 25개 칸에서 모두 시작점을 갖는다.
25가지 케이스 모두, dfs 로 돈다.
가지는 리스트 사이즈가 6이되면 dfs 탈출 -> set() 에 저장
"""
