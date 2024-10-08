from sys import stdin


def number_cards():
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    M = int(input())
    card_pools = list(map(int, input().split()))
    result = [bisect(numbers, number) for number in card_pools]
    return ' '.join(list(map(str, result)))


def bisect(numbers, number):
    left, right = 0, len(numbers),
    while left < right:
        mid = left + (right - left) // 2
        if number == numbers[mid]:
            return 1
        elif number < numbers[mid]:
            right = mid
        else:
            left = mid + 1
    return 0


input = stdin.readline
print(number_cards())

"""
-10 2 3 6 10
"""