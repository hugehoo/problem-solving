import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 입력
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # dict 세팅
    num_dict = {idx + 1: n for idx, n in enumerate(numbers)}
    
    # key 기준 순회
    visited = set()
    result = 0
    for k in num_dict.keys():
        if k in visited:
            continue

        cycle = []
        while k not in visited:
            visited.add(k)
            cycle.append(k)
            k = num_dict[k]
        if cycle:
            result += 1
    print(result)

"""
1
8
3 2 7 8 1 4 5 6

1
10
2 1 3 4 5 6 7 9 10 8
"""
