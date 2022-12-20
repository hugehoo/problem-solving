from itertools import product

# N = int(input())

# 시간 초과
# arr = [[0, 1] for _ in range(N)]
# def check(n):
#     if len(str(n)) != N:
#         return False
#     for idx in range(len(str(n)) - 1):
#         if str(n)[idx] == str(n)[idx + 1] and str(n)[idx + 1] == '1':
#             return False
#     else:
#         return True
# count = 0
# for p in product(*arr):
#     a = ''.join(list(map(str, p)))
#     if check(int(a)):
#         count += 1
# print(count)

# 시작은 1을 박는다.
"""
10 1
10 0
끝이 0으로 끝나면 2개 추가
끝이 1로 끝나면 1개 추
------
100 0
100 1
101 0
------
1000 0
1000 1

1001 0

1010 0
1010 1
------
10000 0
10000 1

10001 0

10010 0
10010 1

10100 0
10100 1

10101 0
-------
(1*2 + 0)2, 3
(1*2 + 1)3, 4 
(2*2 + 1)5, 5
(3*2 + 2)8, 6
(5*2 + 3)13, 7
(8*2 + 5)21, 8
[0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

N = int(input())
right = [0, 0, 0, 1, 1] + [0] * 86
left = [0, 0, 0, 0, 1] + [0] * 86
for i in range(5, N + 1):
    right[i] = right[i - 1] + right[i - 2]
    left[i] = left[i - 1] + left[i - 2]
if N == 2:
    print(1)
elif N == 1:
    print(1)
else:
    print(right[N] * 2 + left[N])