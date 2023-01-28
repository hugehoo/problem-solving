A, K = map(int, input().split())
count = 0

while True:
    if A == K:
        print(count)
        exit()
    if K % 2 == 0 and A <= K // 2:
        K //= 2
    else:
        K -= 1
    count += 1
