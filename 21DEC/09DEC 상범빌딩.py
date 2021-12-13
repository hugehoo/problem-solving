from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:

    L, R, C, = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        exit(0)
    flag = False
    building = []
    for idx in range(L):
        temp = []
        for rdx in range(R):
            case = list(map(str, input()))
            temp.append(case)
        building.append(temp)
        _pass = input()

    queue = deque()
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == "S":
                    queue.append((l, r, c, 0))
                while queue:
                    _l, _r, _c, count = queue.popleft()
                    for i in range(6):
                        nx = _l + dx[i]
                        ny = _r + dy[i]
                        nz = _c + dz[i]
                        if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and (building[nx][ny][nz] == "E"):
                            print(_l, _r, _c)  # 다 다르게 출력된다.
                            print(nx, ny, nz)  # 2 2 0
                            print("Escaped in {0} minute(s).".format(count + 1))
                            # queue = []
                            flag = True

                        if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and (building[nx][ny][nz] == "."):
                            building[nx][ny][nz] = "#"
                            queue.append((nx, ny, nz, count + 1))

    if not flag:
        print("Trapped!")

"""
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0

3 3 3
..S
...
...

...
...
...

...
...
E..
"""
