import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())


def sync(q):
    while q and id_[q[0][1]] == 0:
        heappop(q)


for _ in range(N):
    M = int(input())
    nominate = []
    minq = []
    maxq = []
    number_dict = {}
    id_ = [False] * 1000001

    for m in range(M):
        order, value = map(str, input().strip().split())
        if order == "I":
            heappush(minq, (int(value), m))
            heappush(maxq, (-int(value), m))
            id_[m] = True  # value 가 같은 값이 와도, 입력되는 순서를 기준으로 id_ 를 갱신한다.
        else:
            if value == "1":
                sync(maxq)
                # maxq 를 동기화 -> for what? => minq 에서 제거된 것들이 아직 maxq 에 남아있을 때 지운다. maxq 에 남아있는 것들이 여러개일 수 있으므로,while 문 사용.
                if maxq:
                    pop = heappop(maxq)
                    id_[pop[1]] = False
            else:
                sync(minq)
                if minq:
                    pop = heappop(minq)
                    id_[pop[1]] = False
    sync(maxq)
    sync(minq)

    if maxq and minq:
        print(-maxq[0][0], minq[0][0])
    else:
        print("EMPTY")


"""
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
"""
