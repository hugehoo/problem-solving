import sys

input = sys.stdin.readline
'''

1, 2,  3, 4, 5
-1, 1, -1, 2, 1

6, 7, 8, 9, 10,
3, 2, 4, 3,  2,

11, 12, 13, 14, 15,
 4,  3,  5,  4,  3,

16, 17, 18, 19, 20
 5,  4,  6,  5,  4
 
 21, 22, 23, 24, 25
  6,  5,  7,  6,  5

26, 27, 28, 29, 30
 7,  6,  8
  
rest =>
0 : 5배수
1 :

걍 5배수로 만들어버려
'''

N = int(input())
if N == 1 or N == 3:
    print(-1)
    exit(0)

q, r = divmod(N, 5)
if r == 0:
    print(q)
if r == 1 or r == 4:
    print(q + 2)
if r == 2:
    print(q + 1)
if r == 3:
    print(q + 3)
