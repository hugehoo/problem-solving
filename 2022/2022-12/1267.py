N = int(input())
arr = list(map(int, input().split()))


def method(arr: list, brr: list):
    result = 0
    for a in arr:
        r = a // brr[0]
        result += ((r + 1) * brr[1])
    return result


y = method(arr, [30, 10])
m = method(arr, [60, 15])

if y > m:
    print("M", m)
elif y < m:
    print("Y", y)
else:
    print("Y M", m)


"""
30초 마다
-> 0 ~ 29, 30 ~ 59, 60 ~ 79

60초 마다
0 ~ 59, 60 ~ 119, 120 ~ 179
"""
