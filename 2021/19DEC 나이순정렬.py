# arr = []
# for _ in range(int(input())):
#     age, name = input().split()
#     arr.append((int(age), name))
# arr.sort(key=lambda x: x[0])
# for age, name in arr:
#     print(age, name)
#
from sys import stdin, stdout

arr = [[] for _ in range(201)]

for line in stdin.read().splitlines(True)[1:]:
    arr[int(line.split()[0])].append(line)

stdout.write(''.join(
    ''.join(u) for u in arr
))
"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""