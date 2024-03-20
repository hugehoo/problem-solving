import sys

input = sys.stdin.readline
N = int(input().strip())
remainder = 1000 - N
money = [500, 100, 50, 10, 5, 1]

count = 0
for m in money:
    quotient, remainder = divmod(remainder, m)
    count += quotient
    if remainder == 0:
        break
print(count)


