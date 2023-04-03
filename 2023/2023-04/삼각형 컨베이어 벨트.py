from collections import deque

N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(3)]
b, r = divmod(T, N)
if r == 0:
    if b % 3 == 1:
        print(*belt[2])
        print(*belt[0])
        print(*belt[1])
    elif b % 3 == 2:
        print(*belt[1])
        print(*belt[2])
        print(*belt[0])
    else:
        print(*belt[0])
        print(*belt[1])
        print(*belt[2])
else:
    queue1 = deque(belt[0])
    queue2 = deque(belt[1])
    queue3 = deque(belt[2])
    n = T % N
    for _ in range(n):
        p1 = queue1.pop()
        p2 = queue2.pop()
        p3 = queue3.pop()
        
        queue1.appendleft(p3)
        queue2.appendleft(p1)
        queue3.appendleft(p2)
    
    if b % 3 == 1:
        print(*queue3)
        print(*queue1)
        print(*queue2)
    elif b % 3 == 2:
        print(*queue2)
        print(*queue3)
        print(*queue1)
    else:
        print(*queue1)
        print(*queue2)
        print(*queue3)
"""
T 가 N 의 1배수 면 -> 한 층을 움직임
2배수면 -> 두 층을 움직임
3배수면 원상태
b == 1 -> 한 층을 다 움직임
b = 2 -> 두 층을 다 움직임
b = 3, 0 -> 세 층을 다 움직임
b = 4 -> 세층을 모두 움직이고, 다시 한층을 움직임 : b % 3
"""
