import sys

input = sys.stdin.readline
n, m = map(int, input().split())
left, right = 1, m
total = 0

for _ in range(int(input())):
    position = int(input())
    if left <= position <= right:
        continue
    
    if position < left:
        distance = left - position
        total += distance
        right -= distance
        left = position
    else:  # right < position
        distance = position - right
        total += distance
        left += distance
        right = position
print(total)
