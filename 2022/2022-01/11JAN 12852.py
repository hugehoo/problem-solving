# from sys import stdin
#
# read = stdin.readline
# n = int(read())
# dp = [0] * (n + 1)
# queue = [n]
# def recursive(n, queue):
#     if n < 1:
#         return False
#     if n == 1:
#         return [n, queue]
#     if n % 3 == 0:
#         a = n // 3
#         dp[a] = dp[n] + 1
#         queue.append(a)
#         recursive(a, queue)
#     if n % 2 == 0:
#         a = n // 2
#         dp[a] = dp[n] + 1
#         queue.append(a)
#         recursive(a, queue)
#     a = n - 1
#     queue.append(a)
#     return recursive(a, queue)
# answer = recursive(n, queue)

# queue 를 어떻게 분리시키는가.
# 꼭 queue 를 분리시켜야하나?

# recursive 의 인자로 n 과 count 를 넣자

"""
N = int(input())

result = [[0, []] for _ in range(N + 1)]  # [최솟값, 경로 리스트]
result[1][0] = 0  # 최솟값
result[1][1] = [1]  # 경로를 담을 리스트

for i in range(2, N + 1):

    # f(x-1) + 1
    result[i][0] = result[i - 1][0] + 1
    result[i][1] = result[i - 1][1] + [i]

    # f(x//3) + 1
    if i % 3 == 0 and result[i // 3][0] + 1 < result[i][0]:
        result[i][0] = result[i // 3][0] + 1
        result[i][1] = result[i // 3][1] + [i]

    # f(x//2) + 1
    if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
        result[i][0] = result[i // 2][0] + 1
        result[i][1] = result[i // 2][1] + [i]

print(result[N][0])
for i in result[N][1][::-1]:  # 뒤집은 뒤 출력
    print(i, end=' ')
"""


# for 반복문 - 배열 사용
# N = int(input())
# dp = [[0, []] for _ in range(N + 1)]
# dp[1][1] = [1]
#
# for i in range(2, N + 1):
#     dp[i][0] = dp[i - 1][0] + 1
#     dp[i][1] = dp[i - 1][1] + [i]
#
#     if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
#         dp[i][0] = dp[i // 3][0] + 1
#         dp[i][1] = dp[i // 3][1] + [i]
#
#     if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
#         dp[i][0] = dp[i // 2][0] + 1
#         dp[i][1] = dp[i // 2][1] + [i]
#
# print(dp[N][0])
# print(*dp[N][1][::-1])

def solution():
    visited = []
    queue = [[N, [N]]]

    while queue:
        number, path = queue.pop(0)
        if number == 1:
            print(queue)
            print(len(path) - 1)
            print(" ".join(map(str, path)))
            break

        if number not in visited:
            visited.append(number)
            if number % 3 == 0:
                queue.append([number // 3, path + [number // 3]])
            if number % 2 == 0:
                queue.append([number // 2, path + [number // 2]])
            queue.append([number - 1, path + [number - 1]])


N = int(input())
solution()
