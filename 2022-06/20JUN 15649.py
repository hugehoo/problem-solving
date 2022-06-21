import sys

input = sys.stdin.readline

def check2(x):
    if x == m + 1:
        print(arr[1:])
        return
    else:
        for i in range(1, n + 1):
            if not visit[i]:
                visit[i] = 1
                arr[x] = i
                check(x + 1)
                visit[i] = 0
                arr[x] = 0

def check(x):
    if x == m + 1:
        print(*arr[1:])
        return
    else:
        for i in range(1, n + 1):
            if not visit[i]:
                visit[i] = 1
                arr[x] = i
                check(x + 1)
                arr[x] = 0
                visit[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    visit = [0] * (n + 1)
    arr = [0] * (m + 1)
    check(1)
