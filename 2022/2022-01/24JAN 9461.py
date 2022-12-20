from sys import stdin

read = stdin.readline
N = int(read())

for _ in range(N):
    M = int(read())
    data = [1] * (M + 1)
    if M <= 3:
        print(1)
        continue  # 이걸 break 로 해둬서 계속 틀렸던 거임..
    for m in range(3, M + 1):
        data[m] = data[m - 2] + data[m - 3]
    print(data[M - 1])
