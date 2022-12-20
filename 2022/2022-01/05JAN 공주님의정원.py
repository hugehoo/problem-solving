from sys import stdin

read = stdin.readline

N = int(read())
result = []
start_base, end_base = '0301', '1130'


def to_str_date(a):
    first, second = '', ''
    for i, j in zip(a[:2], a[2:]):
        if len(i) == 1:
            i = '0' + i

        if len(j) == 1:
            j = '0' + j

        first += i
        second += j

    return first, second


for _ in range(N):
    a = list(map(str, read().split()))
    start, end = to_str_date(a)
    result.append((start, end))
# result = sorted(result, key=lambda x: x[0])
# result = sorted(result, key=lambda x: x[1])
result = sorted(result, key=lambda x: (x[0], x[1]))
# [('0101', '0531'), ('0101', '0630'), ('0515', '0831'), ('0610', '1210')]

for s, e in result:
    if s > start_base:
        continue
    else:
        print(s, e)


print(result)

"""
4
1 1 6 30
5 15 8 31
6 10 12 10
1 1 5 31
"""
