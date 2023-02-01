N, T, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
else:
    nums = list(map(int, input().split()))
    if N == P and nums[-1] >= T: # 그러니까, 주어진 수와 리미트가 같으면서 마지막 수보다 T 가 작으면 -1 이다. 아 P 가 N 보다 작을리는 없구나.
        print(-1)
    else:
        result = N + 1
        for n in range(N):
            if nums[n] <= T:
                result = n + 1
                break
        print(result)
