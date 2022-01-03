import heapq
import sys

N = int(sys.stdin.readline())
result_dict = {}
for _ in range(N):
    m = int(sys.stdin.readline())
    result_dict[m] = result_dict.get(m, 0) + 1
res0 = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))
res1 = sorted(list(map(lambda x: (-x[1], x[0]), result_dict.items())))
print(res0)
print(res0[0][0])
