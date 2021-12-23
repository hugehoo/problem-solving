def gcd(a, b):
    while b != 0:
        n = a % b
        a, b = b, n
        # b = n
    return a


N = int(input())
arr = list(map(int, input().split()))
base = arr[0]

for i in range(1, N):
    result = gcd(base, arr[i])
    print("{0}/{1}".format(base // result, arr[i] // result))

# base = arr[0]
# for i in range(1, N):
#     b, r = divmod(base, arr[i])
#     if r == 0:
#         print(''.join(map(str, [base // arr[i], '/', 1])))
#     else:
#         while True:
#             b, _r = divmod(base, arr[i])
#             if _r == 0:
#                 break
#             else:
#                 base
#
#         if _r == 0:
#             print(''.join(map(str, [base // r, '/', arr[i] // r])))
#         else:
#             print(''.join(map(str, [base, '/', arr[i]])))


"""
4
7 12 14 28

7/12
1/2
1/4

4
12 3 8 4

4/1
3/2
3/1

4
300 1 1 300
"""
