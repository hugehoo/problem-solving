from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    T = int(input().rstrip())
    for _ in range(T):
        N = int(input().rstrip())
        arr = list(map(int, input().split()))
        latest = arr[-1]
        result = 0
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < latest:
                result += (latest - arr[i])
            else:
                latest = arr[i]
        print(result)
