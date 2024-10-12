from sys import stdin


def room(T):
    times = [list(map(int, input().split())) for _ in range(T)]
    times.sort(key=lambda x: (x[1], x[0]))
    count, last = 0, 0
    for start, end in times:
        if start >= last:
            count += 1
            last = end
    return count


input = stdin.readline
T = int(input())
print(room(T))

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
