import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(M)]
temp = sorted(temp, key=lambda x: (x[0], x[1],))

"""
사야할 갯수가 6개 이하일 때 분기 처리
"""
n, r = divmod(N, 6)
answer = n * temp[0][0]
if r * temp[0][1] > temp[0][0]:
    val = temp[0][0]
    temp = sorted(temp, key=lambda x: x[1])

    if val > temp[0][1] * r:
        answer += (r * temp[0][1])
        print(answer)
        exit(0)
    else:
        answer += val
        print(answer)
        exit(0)
else:
    temp = sorted(temp, key=lambda x: x[1])
    answer += (r * temp[0][1])
    print(answer)
