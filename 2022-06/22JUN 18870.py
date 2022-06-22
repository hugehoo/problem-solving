import sys

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))
num_dict = {}

sorted_arr = sorted(list(set(arr)))

for idx, s in enumerate(sorted_arr):
    num_dict[s] = idx

for a in arr:
    print(num_dict[a], end=" ")
