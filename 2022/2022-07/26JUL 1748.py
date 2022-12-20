T = int(input())

# 1.
# length = 0
# for i in range(1, T + 1):
#     length += len(str(i))
# print(length)

# 2.
# len_dict = {}
# for i in range(1, T + 1):
#     len_dict[len(str(i))] = len_dict.get(len(str(i)), 0) + 1
#
# answer = 0
# for k, v in len_dict.items():
#     answer += (k * v)
# print(answer)

# 3.
length = len(str(T))
answer = 0
if length == 1:
    print(T)
    exit()
previous = length - 1
for i in range(1, previous + 1):
    answer += i * int('9' + '0' * (i - 1))
count = T - int('9' * previous)
answer += (count * length)
print(answer)

"""
1 자리 : 9개
2 자리 : 90개
3 자리 : 900개
4 자리 : 90000개
"""
