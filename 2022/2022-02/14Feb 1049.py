import sys
from math import inf

input = sys.stdin.readline
n, m, = map(int, input().split())


def solve():
    min1 = inf
    min6 = inf

    for _ in range(m):
        six, one = map(int, input().split())
        min1 = min(min1, one)
        min6 = min(min6, six)

    if min6 > min1 * 6:  # 낱개로 사는 것이 묶음 보다 싼 경우
        return n * min1
    elif min6 < min1:  # 묶음이 1개보다 싼 경우
        return (n // 6) * min6 + (min6 if n % 6 else 0)
    else:  # 묶음이 낱개 세트 보다 싼 경우 -> min6 < min1 * 6
        n_ = n % 6
        return (n // 6) * min6 + (min(n_ * min1, min6) if n % 6 else 0)


print(solve())
# heap = []
# arr = []
# for _ in range(m):
#     six_pack, one = map(int, input().split())
#     arr.append(one)
#     heapq.heappush(heap, (six_pack / 6, six_pack, one))
# arr.sort()
# result = 0
# while n > 0:
#     percent, six, one = heapq.heappop(heap)
#     if percent <= one and n >= 6:
#         n -= 6
#         result += six
#         heapq.heappush(heap, (percent, six, one))
#     elif n < 6:
#         if six > arr[0] * n:
#             result += (arr[0] * n)
#         else:
#             result += six
#         break
#     else:
#         result = one * n
#         n = 0
# print(result)

"""
min6, min1 비교
min6 는 
-> 

min6 -> 가장 작은 것이 가장 저렴한 방법
per 가 min1 보다 작다면 min6 로 계산
if per < min1:
    return (n // 6) * min6 + min6
elif per > min1:
    return n * min1
else:
    return 


6 1
7 1

1 100
7 1
"""
