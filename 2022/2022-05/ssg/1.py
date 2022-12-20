from heapq import heappop, heappush


def solution(v, a, b):
    hq = []
    for i in range(len(v)):
        heappush(hq, (-v[i], v[i]))
    count = 0
    while hq:
        if hq[0][1] < a:
            return count

        idx, value = heappop(hq)
        value -= a
        for i in range(len(hq)):
            jdx, value2 = hq[i]
            if value2 < b:
                return count
            value2 -= b
            hq[i] = (-value2, value2)

        heappush(hq, (-value, value))
        count += 1



""" 

최대 힙 -> pop a 만큼 감소
나머지는 b 만큼 감소 -> how ?

"""
print(solution([4, 5, 5], 2, 1))
print(solution([4, 4, 3], 2, 1))
