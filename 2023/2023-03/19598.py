from heapq import heappop, heappush

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: x[0])

rooms = [0]
count = 1
for t in times:
    if t[0] >= rooms[0]:
        heappop(rooms)
    else:
        count += 1
    heappush(rooms, t[1])
print(count)

"""
이중 for 문을 어떻게 없앴느냐?
heapq 를 사용했다.
이중 for 문을 사용한 이유는, 현재 가장 먼저 끝나는 강의 시간을 찾기 위해 rooms 를 순회가 필요했기 때문
그 역할을 heapq 가 대신한다.
heapq 의 첫번째 원소가 가장 먼저 끝나는 강의 시간이기 때문.
즉 두번째 for 문의 역할을 heapq 가 대신하여, 이중 for 문을 없앨 수 있다.
"""
