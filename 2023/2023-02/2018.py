N = int(input())

# 공간복잡도 너무 O(N)
# nums = [i for i in range(1, N + 1)]
# count, end, interval_sum = 0, 0, 0
#
# for start in range(N):
#     while interval_sum < N and end < N:
#         interval_sum += nums[end]
#         end += 1
#     if interval_sum == N:
#         count += 1
#     interval_sum -= nums[start]
# print(count)

interval_sum = 1
count = 1
start, end = 1, 1
while start < (N//2) + 1:
    if interval_sum < N:
        end += 1
        interval_sum += end
        
    if interval_sum == N:
        count += 1
        end += 1
        interval_sum += end
        
    if interval_sum > N:
        interval_sum -= start
        start += 1
        
        
print(count)
        

"""
어케 하지
어떤 경우로 만들 수 있는지는 중요치 않다.
몇가지 경우로 만들 수 있느냐가 포인트
각 경우가 무슨 수로 차있는진 알 필요 없다.

N 은 큰 수
연속된 자연수의 합

two pointer

답은 연속된 수의 합 or 하나의 수로 가능(자기 자신)

나누기 2 한 수부터 시작.


"""
