N = int(input())

count = 0
arr = [500, 100, 50, 10, 5, 1]
N = 1000 - N
for i in arr:
    if N >= i:
        count += (N // i)
        N = N % i
print(count)


"""
1000 - 1 = 999
999 - 500 = 499
499 - 400 = 99
99 - 90 = 9
9 - 9 = 0

500 : 500 * 1
400 : 100 * 4
90 : 50 * 1 + 10 * 4
9 : 5 * 1 + 1 * 4
"""