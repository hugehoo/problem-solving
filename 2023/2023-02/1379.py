N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
sorted_lectures = sorted(lectures, key=lambda x: x[1])
for sl in sorted_lectures:
    print(sl)
rooms = [sorted_lectures[0][2]]
K = float("-inf")
print(rooms)
for i, s, e in sorted_lectures[1:]:
    if min(rooms) > s:
        rooms.append(e)
    else:
        min_idx = rooms.index(min(rooms))
        rooms[min_idx] = e
    print(rooms)
    if len(rooms) > K:
        K = len(rooms)

print(K)

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
