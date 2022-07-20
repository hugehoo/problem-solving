from collections import deque


T = int(input())

for _ in range(T):
    con = int(input())
    con_list = deque()

    s_x, s_y = map(int, input().split())
    for _ in range(con):
        c_x, c_y = map(int, input().split())
        con_list.append([c_x, c_y])

    e_x, e_y = map(int, input().split())
    while con_list:
        c_x, c_y = con_list.popleft()
        distance = abs(c_x - s_x) + abs(c_y - s_y)
        if 1000 < distance:
            print("sad")
            exit()
        s_x, s_y = c_x, c_y
    distance = abs(e_x - s_x) + abs(e_y - s_y)
    if 1000 < distance:
        print("sad")
        exit()
    print("happy")


"""
1
2
0 0
-450 -250
-600 500
-600 1000

1
2
0 0
-1000 0
1000 0
2000 0

1
0
0 0
2000 0

1
0
0 0
1000 0
"""