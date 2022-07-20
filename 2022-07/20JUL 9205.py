T = int(input())

for _ in range(T):
    con = int(input())
    con_list = []

    s_x, s_y = map(int, input().split())
    for _ in range(con):
        c_x, c_y = map(int, input().split())

        distance = abs(c_x - s_x) + abs(c_y - s_y)
        if 1000 < distance:
            print("sad")
            exit()
        con_list.append([c_x, c_y])
        s_x, s_y = c_x, c_y

    e_x, e_y = map(int, input().split())
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
"""