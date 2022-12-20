import sys

input = sys.stdin.readline

n = int(input())

a = 300
b = 60
c = 10

a_b, a_r = n // a, n % a
b_b, b_r = a_r // b, a_r % b
c_b, c_r = b_r // c, b_r % c

if c_r != 0:
    print(-1)
else:
    print(a_b, b_b, c_b)