N = int(input())
arr = [0] * 10001
arr[1] = 1
arr[2] = 1
arr[3] = 2

if N <= 3:
    print(arr[N])
    exit()

for n in range(4, N + 1):
    arr[n] = arr[n - 1] + arr[n - 2]
print(arr[N])
