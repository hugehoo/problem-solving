from sys import stdin

input = stdin.readline


def binary_search(nums: list, target: int):
    s, e = 0, len(nums) - 1
    while s <= e:
        mid = ((s + e) // 2)
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return 0


if __name__ == '__main__':
    N = int(input().rstrip())
    arr = list(map(int, input().split()))
    arr.sort()
    
    M = int(input().rstrip())
    arr2 = list(map(int, input().split()))
    result = [0] * M
    for idx, a in enumerate(arr2):
        if binary_search(arr, a):
            result[idx] = 1
    print(*result)
