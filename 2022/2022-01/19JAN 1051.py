N, M, = map(int, input().split())
if N == 1 or M == 1:
    print(1)
    exit()

arr = [list(map(int, input())) for _ in range(N)]
# 한 행의 길이와 set 로 만들었을 때 길이가 같다면, 그 줄은 그냥 스킵해도 됨.

non_nominate = []
temp = []
for rdx, r in enumerate(arr):
    if len(r) == len(set(r)):
        continue
    for cdx, c in enumerate(r):
        if c not in r:
            continue
        # else:
        #     temp.append(r.index(c))
        # print((rdx, cdx), 'c = ', c)


# tm = [1,2,3,4,5,6,1]
# tm.count(1)
def check(r, c, _r, _c, diff):
    if arr[r + diff][c] == arr[r][c] and arr[r][_c + diff] == arr[r][_c]:
        return True
    else:
        return False
