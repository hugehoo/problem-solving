import sys

input = sys.stdin.readline

N = int(input())
new_arrays = sorted([list(input().strip()) for _ in range(N)], key=lambda x: len(x), reverse=True)
alpha_dict = {}
answer = 0
num = 9

for na in new_arrays:
    M = len(na)
    for i in range(M):
        value = 10 ** (M - i - 1)
        if alpha_dict.get(na[i], 0) == 0:
            alpha_dict[na[i]] = value
        else:
            alpha_dict[na[i]] += value

for v in sorted(alpha_dict.values(), reverse=True):
    answer += v * num
    num -= 1
print(answer)
