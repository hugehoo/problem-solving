N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

while sum(arr) != 0:
    check = 0
    for i in range(N):
        if arr[i] % 2 != 0 or arr[i] == 0 or arr[i] == 1:
            if arr[i] == 0:
                continue
            else:
                arr[i] -= 1
                cnt += 1
            check = 1

    if not check:
        for n in range(N):
            arr[n] //= 2
        cnt += 1
print(cnt)

"""
1, 2, 4, 8, 16, 32, 33, 34, 35, 
1, 2, 4, 8, 9, 10, 11, 12, 24, 25, 50, 100  
1, 2, 3, 6, 12, 24, 25, 50, 100
"""
