import sys

read = sys.stdin.readline
N = int(read())
arr = list(map(int, read().split()))
count = 0
for i in arr:
    # if i == 2 or i == 3:
    #     count += 1
    if i <= 1:
        continue
    # if i >= 4:
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break
    else:
        count += 1
print(count)

"""
4
1 3 5 7
"""
