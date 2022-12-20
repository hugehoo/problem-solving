N = int(input())


def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recursive(n - 1) + recursive(n - 2) + recursive(n - 3)


for _ in range(N):
    print(recursive(int(input())))

"""
3
4
7
10

1, 2, 3
"""
