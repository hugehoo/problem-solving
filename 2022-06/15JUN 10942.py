import sys

input = sys.stdin.readline


def palindrome(arr: list):
    m = len(arr) // 2
    if len(arr) % 2 == 0:
        if arr[0:m] == arr[m: len(arr)][::-1]:
            return 1
        return 0
    else:
        if arr[0:m] == arr[m + 1: len(arr)][::-1]:
            return 1
        return 0


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(palindrome(arr[a - 1: b]))

"""
palindrome 인지 아닌지만 판별하면 된다. 어떻게?
dp = []
어떤 인덱스에서 몇번째까지 팰린드롬인지. 나오지 않을까? 한 인덱스를 기준으로 팰린드롬이 여러개 나올 수 있나?
 
"""