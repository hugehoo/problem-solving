from collections import defaultdict

D = int(input())
count = 0

campus = defaultdict(list)
campus[1] = [2, 3]
campus[2] = [1, 3, 4]
campus[3] = [1, 2, 4, 5]
campus[4] = [2, 3, 5, 6]
campus[5] = [3, 4, 6, 7]
campus[6] = [4, 5, 8]
campus[7] = [5, 8]
campus[8] = [6, 7]


def recursive(start, d):
    global count
    if d < 0:
        return
    if d == 0 and start == 1:
        count += 1
        return
    for s in campus[start]:
        recursive(s, d - 1)


recursive(1, D)
print(count % 1_000_000_007)
"""
재귀 함수 -> 현재 시작점. 남은 회수 인자로 받음. 회수 인자가 0일 때, 현재 시작점이 다시 1이여야 true.
이럴때 global 변수 count 를 +1
def recursive(start, d):
    if d < 0:
        return
    if d == 0 and start == 1:
        count += 1
        return;
    for start` in array[start]:
        recursive(start`, d - 1)

array 라는 딕셔너리를 만들어야한다.
동일한 경로를 가지 않았다고 어떻게 체크할까.
시간 초과 남. 어떻게 visit 경로를 저장할까.

어떻게 경우의 수를 만들지.
1에서 시작하여, 다시 1로 돌아오는 경우의 수.
모든 경우의 수를 만들어 본다하더라도, 어떻게 경우를 만드는것인가

dp ->
D 만큼 배열을 만든다.
ex) d = 4
[0, 1, 2, 3, 4]
[0, 0, 2, 0, 0]


출발점에서 다시 출발점으로 돌아오기까지 거쳐야하는 이동하는 회수가 D개인 경로의 수
"""
