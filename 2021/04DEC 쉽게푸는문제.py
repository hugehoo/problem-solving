start, end = map(int, input().split())
arr = [i for i in range(1, end + 1) for _ in range(1, i + 1)]
print(sum(arr[start - 1: end]))



