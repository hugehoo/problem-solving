import sys

input = sys.stdin.readline

string = input()
N = len(string)
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
i = 0
while i < N:
    if string[i:i + 2] in ["c=", "c-", "d-", "lj", 'nj', 's=', 'z=']:
        count += 1
        i += 2
        continue
    if string[i: i + 3] in ["dz="]:
        count += 1
        i += 3
        continue
    count += 1
    i += 1
print(count - 1)
"""
ljes=njak
ddz=z=
nljj
"""
