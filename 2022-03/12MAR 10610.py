import sys
from itertools import permutations

input = sys.stdin.readline

# 1
# t = list(input().rstrip())
# t.remove('0')
# max_v = max(t)
# result = []
# for i in permutations(t, len(t)):
#     stringNumber = ''.join(i)
#     if len(str(int(stringNumber))) == len(i) and int(stringNumber) % 3 == 0 and stringNumber[0] == max_v:
#         result.append(int(stringNumber))
# print(str(max(result)) + '0')


# 2
# number = input().strip()
# number_list = list(map(int, number))
# number_list.sort()
#
# sum_num = sum(number_list)
# string = ''
# if (number_list[0] == 0) and sum_num % 3 == 0:
#     for number in number_list:
#         string += str(number)
#     print(int(string[::-1]))
#         # string = str(number) + string
#     # print(int(string))
# else:
#     print(-1)

# 3
# n = input()
# arr, total = [0] * 10, 0
#
# for i in range(10):
#     arr[i] = n.count(str(i))
#     total += (arr[i] * i)
#
# if arr[0] == 0 or total % 3 != 0:
#     print(-1)
# else:
#     for i in range(10):
#         print(str(9 - i) * arr[9 - i], end='')

# 4
n = list(map(int, input().strip()))
total = sum(n)
if n.count(0) == 0 or total % 3 != 0:
    print(-1)
    exit()
n.sort(reverse=True)
for i in n:
    print(str(i), end='')

"""
100_000 개의 숫자로 구성됨
"""
