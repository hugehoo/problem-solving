import sys
from collections import Counter


input = sys.stdin.readline


def get_median_v2(data):
    data = sorted(data)
    centerIndex = len(data) // 2
    return data[centerIndex]


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

cnt = Counter(arr)
sorted_cnt = sorted(cnt.items(), reverse=True)
print(sorted_cnt[0], sorted_cnt[1])
print(cnt.values())

print(round(sum(arr) / n))
print(get_median_v2(arr))
print()
print(abs(max(arr) - min(arr)))
