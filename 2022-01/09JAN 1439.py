# import copy
# N = input()
# M = copy.deepcopy(N)
#
# # 0 기준
# N = N.split('0')
# print(N)
#
# count = 0
# flag = False
# for n in N:
#     if flag:
#         if n == '':
#             flag = True
#         else:
#             flag = False
#             count += 1
#
#     if n == '':
#         flag = True
#     else:
#         flag = False
# if N[-1] == '':
#     count += 1
# print(count)
#
# # 1 기준
# M = M.split('1')
# print(M)
# one_count = 0
# flag = False
# for n in M:
#     if flag:
#         if n == '':
#             flag = True
#         else:
#             flag = False
#             one_count += 1
#
#     if n == '':
#         flag = True
#     else:
#         flag = False
# if M[-1] == '':
#     one_count += 1
# print(one_count)
# print(min(count, one_count))

N = input() + '-'
previous = []
result = []
for n in N:
    if not previous:
        previous.append(n)
    if previous and previous[-1] == n:
        previous.append(n)
    else:
        result.append(previous[-1])
        previous = [n]
print(min(result.count('1'), result.count('0')))

"""
11001100110011000001
"""