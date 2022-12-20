from sys import stdin


N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
count = 0
left, right = 0, 1
# M 이랑 매칭될 때까지 차례로 더하거나
# M 보다 커지면 break
# 어떻게 M 을 맞추느냐는 관심없다. 몇가지 연속된 숫자의 경우가 M 을 맞추는지가 중요.
if arr[0] == M:
    count += 1

while right < len(arr):
    total = sum(arr[left: right + 1])
    if total < M:
        right += 1
    elif total > M:
        left += 1
    else:
        print('count ', count, ', left ', left, ' right ', right)
        count += 1
        left += 1
        right += 1

# for i in range(N):
#     for j in range(i + 1, N + 1):
#         temp = sum(arr[i:j])
#         if temp == M:
#             count += 1
#             break
#         elif temp > M:
#             break
print(count)

"""
10 5
1 2 3 4 2 5 3 1 1 2
"""