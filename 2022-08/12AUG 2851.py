import sys

input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]
count = 0
answer = []
for i in range(10):
    before = count
    count += arr[i]
    if abs(100 - before) >= abs(100 - count):
        answer.append(count)
    else:
        continue
print(max(answer))
"""
40
40
40
40
40
40
40
40
40
40
"""
