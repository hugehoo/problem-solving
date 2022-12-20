import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())

answer, positive, negative = [], [], []
pop, pop_ = 0, 0

for _ in range(N):
    num = int(input())
    if num <= 0:
        heappush(negative, num)
    else:
        heappush(positive, [-num, num])

while negative:
    if len(negative) > 1:
        pop1 = heappop(negative)
        pop2 = heappop(negative)
        answer.append(max(pop1 * pop2, pop1 + pop2))
    elif len(negative) == 1:
        answer.append(heappop(negative))

while positive:
    if len(positive) > 1:
        pop1 = heappop(positive)
        pop2 = heappop(positive)
        answer.append(max(pop1[1] * pop2[1], pop1[1] + pop2[1]))

    elif len(positive) == 1:
        answer.append(heappop(positive)[1])
print(sum(answer))

"""
case.1
양수 밖에 없을 때 -> 그냥 소팅하면 된다.

case.2 
음수 밖에 없을 때 -> reverse 소팅하면 된다.

case.3
음수 양수 섞여 있을 때. => 절대값 큰 순서대로 소팅 -> ㄴㄴ -> 음수는 음수끼리 곱한다. 무조건 곱해야하나? 

음수 양수를 따로 리스트 만들자. 
"""
