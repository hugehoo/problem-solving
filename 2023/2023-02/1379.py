import heapq
from heapq import heappush, heappop

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
sorted_lectures = sorted(lectures, key=lambda x: x[1])
room = [i for i in range(1, N + 1)]
pq = []
answer = [0] * (N + 1)
for i, start, end in sorted_lectures:
    while pq and pq[0][0] <= start:
        end, roomNo = heappop(pq)
        heappush(pq, [])
        
    r, room = room[0], room[1:]
    heappush(pq, [start, r])
    answer[i] = r

# for i, s, e in sorted_lectures:
#     if pq and pq[0][0] <= s:
#         heappop(pq)
#         heappush(pq, [e, s, i])
#         room[i] = K
#     else:
#         heappush(pq, [e, s, i])
#         K += 1
#         room[i] = K
# 강의실 번호는 일찍 들어가는 순서대로 할당해도 된다.
print(K)
print(' ')
print(room)

"""
강의 번호, 시작 시간, 종료 시간

강의 순 출력 ?
1번 강의엔 4번실?


강의 종료 시간 리밋 : 10억
필요한 최소 강의실 수 K

시작 시간이 빠른 순서대로 먼저 배정.
최소 강의실 구하는 것도 어려운데?
{시작, 끝} 입력할 때, 시작은 제외하고 끝만 넣자.

각 강의 마다 강의실 배정.
각 강의에 배정할 강의실 번호


5 : K 개 강의실
4 : 1번 강의는 4번 강의실 사용
3
2
4
1 :
3
4
5

각 강의에 배정할 강의실 번호를 순서대로 출력
1번 강의엔 4번 강의실.
"""
