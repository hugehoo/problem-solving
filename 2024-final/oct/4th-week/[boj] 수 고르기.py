from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = []
    
    for _ in range(N):
        i = int(input().rstrip())
        nums.append(i)
    if N == 1:
        print(M)
        exit(0)

    nums.sort()
    s, e = 0, 1
    max_diff = float('inf')
    while s <= e < len(nums):
        if nums[e] - nums[s] >= M:
            # 조건 만족함. 저장은 해야지.
            max_diff = min(nums[e] - nums[s], max_diff)
            s += 1
        else:
            e += 1
    print(max_diff)
    
"""
7 4
1
8
15
16
17
18
22
"""
