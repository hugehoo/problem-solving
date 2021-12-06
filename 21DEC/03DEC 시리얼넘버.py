def countNumber(M):
    sum_ = 0
    for m in M:
        try:
            sum_ += int(m)
        except ValueError:
            pass
    return sum_


def __main__():
    N = int(input())
    arr = []

    for _ in range(N):
        M = input()
        total = countNumber(M)
        arr.append((M, len(M), total))

    arr.sort(key=lambda x: (x[1], x[2], x[0]))

    for i in arr:
        print(i[0])


__main__()

"""
5
ABCD
145C
A
A910
Z321
"""