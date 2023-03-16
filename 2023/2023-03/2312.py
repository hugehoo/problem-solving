T = int(input())
for _ in range(T):
    N = int(input())
    nums = [False, False] + [True] * (N - 1)
    for i in range(2, N + 1):
        if nums[i]:
            for j in range(2 * i, N + 1, i):
                nums[j] = False
    num_dict = {}
    for idx, t in enumerate(nums):
        if t:
            while True:
                b, r = divmod(N, idx)
                if not r:
                    num_dict[idx] = num_dict.get(idx, 0) + 1
                    N = b
                else:
                    break
    keys = sorted(num_dict.keys(), key=lambda x: x)
    for k in keys:
        print(k, num_dict.get(k))
