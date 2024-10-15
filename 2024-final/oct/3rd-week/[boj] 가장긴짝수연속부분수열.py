from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    total_length, K = map(int, input().split())
    nums = list(map(int, input().split()))
    left_pointer, right_pointer = 0, 0
    odd_count, result = 0, 0
    while right_pointer < total_length:
        if odd_count <= K:
            if nums[right_pointer] % 2 == 1:  # right_pointer 가 홀수일 때
                odd_count += 1
            right_pointer += 1
        else:
            if nums[left_pointer] % 2 == 1:  # left_pointer 가 홀수일 때
                odd_count -= 1
            left_pointer += 1
            continue
        result = max(result, right_pointer - left_pointer - odd_count)
    print(result)
"""
삭제할 수 있는 최대 K
가장 긴 짝수 길이

같이 시작해도 되지않나?
홀수 나오면 삭제,

"""
