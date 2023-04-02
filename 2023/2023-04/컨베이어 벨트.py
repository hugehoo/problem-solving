from collections import deque

N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]
if (T % (N * 2)) == 0:
    print(*belt[0])
    print(*belt[1])
elif T % N == 0:
    print(*belt[1])
    print(*belt[0])
else:
    b, r = divmod(T, N)
    move = r
    queue0 = deque(belt[0])
    queue1 = deque(belt[1])
    for _ in range(move):
        queue0.appendleft(queue1.pop())
        queue1.appendleft(queue0.pop())
    if b % 2 == 0:
        print(*list(queue0))
        print(*list(queue1))
    else:
        print(*list(queue1))
        print(*list(queue0))

# 1) T가 N*2 의 배수만큼이면, 원상태가 된다.
# 2) T % N == 0 이면 위 아래 스위치
# 위 둘은 하나의 if else 에 묶여야함.
