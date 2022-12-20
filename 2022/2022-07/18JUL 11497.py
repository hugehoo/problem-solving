T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = 0
    for j in range(2, N):
        result = max(result, abs(arr[j] - arr[j - 2]))
    print(result)


"""
2 5 9 7 4 -> 인접 수 최대 차이 : 4 => 다른 배열 에서는 인접 수 사이의 최대 차이를 4보다 작게 만들 수 없다.
2 4 5 7 9  
"""



