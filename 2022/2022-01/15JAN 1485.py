N = int(input())
for _ in range(N):
    arr = sorted([list(map(int, input().split())) for _ in range(4)])
    if arr[0][0] == arr[1][0] and abs(arr[0][1] - arr[1][1]) == abs(arr[2][1] - arr[3][1]) and arr[2][0] == arr[3][0]:
        print(1)
    elif arr[0][1] == arr[3][1] and abs(arr[0][0] - arr[3][0]) == abs(arr[1][1] - arr[2][1]) and arr[1][0] == arr[2][0]:
        print(1)
    else:
        print(0)
