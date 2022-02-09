import sys


input = sys.stdin.readline().rstrip

N = input()
# print(N)
# length = len(N)
letters = set()
# for j in range(1, length + 1):
#     for i in range(length):
#         letters.add(''.join(N[i:i + j]))
for i in range(len(N)):
    for j in range(i, len(N)):
        letters.add(N[i:j + 1])
print(len(letters))
# print(letters)



"""
01, 12, 23, 34, 45
02, 13, 
"""

