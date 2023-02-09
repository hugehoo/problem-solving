N = int(input())
numbers = [input() for _ in range(N)]
i = 1

while True:
    if len(set(map(lambda x: x[-i:], numbers))) == N:
        print(i)
        exit(0)
    i += 1

"""
N 이 한자리 일 때 예외 발생
3
1
2
3

4
12312
19312
32310
10201

5
12312
19312
32310
10201
16301
"""
