"""
큐 - FIFO

a b c d e

b e d a c


a b c d e

e c a b d
2

"""

# from collections import deque
#
# answer = 0
# n = int(input())
# q1 = deque()
#
# for i in range(n*2):
#     if i < n:
#         q1.append(input())
#     else:
#         out = input()
#         if out != q1[0]:
#             q1.remove(out)
#             answer += 1
#         else:
#             q1.popleft()
# print(answer)

N = int(input())
Entry = {input().rstrip(): i for i in range(N)}
Exit = list(int(Entry[input().rstrip()]) for _ in range(N))
res = 0
print(Exit)
for i in range(N):
    if Exit[i] >= len(Exit[i + 1:]):
        print(i, Exit[i], Exit[i + 1:])
        res += 1
print(res)
# a b c d e
# 5 3 1 2 4