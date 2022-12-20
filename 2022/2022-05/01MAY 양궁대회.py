from collections import deque
from itertools import combinations_with_replacement


def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0
    for res in list(combinations_with_replacement(range(0, 11), n)):
        ryan_info = [0 for _ in range(11)]
        for r in res:
            ryan_info[10 - r] += 1

    # combinations_with_replacement -> 중복 가능한 조합 -> [0, 0, 0, 0, 1] 의 의미는 0번째를 4번 쏘고, 1번재를 1번 쐈다는 의미.
    # 총 n(=5)번 쏜것이 된다.
    for res in list(combinations_with_replacement(range(0, 11), n)):
        now = [0 for _ in range(11)]
        for r in res:
            now[10 - r] += 1
        ryan = 0
        peach = 0

        for i, (r, p) in enumerate(zip(now, info)):
            if r == p == 0:
                continue
            if p >= r:
                peach += (10 - i)
            elif r > p:
                ryan += (10 - i)
        if ryan > peach:
            win = True
            if (ryan - peach) > max_num:
                max_num = ryan - peach
                answer = now
    if not win:
        return [-1]
    return answer


"""
info 는 먼저 주어진다.
가장 큰 점수 차이로 '이기는 것' 이 목표
우선 이기는 경우의 수를 모두 만들어봐야한다.
n = 10 이하 이기 때문에 시간복잡도에서 자유로울 수 있다.

각 점수마다 아예 안 맞추거나, 어피치보다 1점 더 높게 맞추는 2가지 경우 존재 
2^11 => 2048가지
"""

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
