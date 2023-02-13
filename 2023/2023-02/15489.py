from itertools import chain


r, c, w = map(int, input().split())
triangle = [[1], [1, 1], [1, 2, 1]]
answer = 0

for i in range(3, r + w):
    temp = []
    for idx, v in enumerate(range(i + 1)):
        if idx == 0 or idx == i:
            temp.append(1)
        else:
            temp.append(triangle[i - 1][idx - 1] + triangle[i - 1][idx])
    triangle.append(temp)

answer = [triangle[row][c - 1:c + idx] for idx, row in enumerate(range(r - 1, r + w - 1))]

print(sum(chain.from_iterable(answer)))
# print(sum(sum(answer, [])))

"""
r: 줄 번호
c: r 줄의 c 번째 수
w: c를 포함하는 삼각형의 변 길이
r + w = 만들어야  할 삼각형 길이
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""
