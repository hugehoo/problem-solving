import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    temp = []
    for _ in range(int(input())):  # 100_000
        a, b = map(int, input().split())
        temp.append((a, b))
    temp.sort()

    count = 0
    base = temp[0][1]

    for t in temp:
        print(t, temp[0])

        if t[1] < base:  # t[1] 이 base 보다 작은 경우를 생각하기 보단, t[1] 이 한번이라도 bae보다 크면 선발되지 않는다고 생각했다.
            count += 1
            print('t[1]', t[1])
            base = t[1]
    print(count)


"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""
