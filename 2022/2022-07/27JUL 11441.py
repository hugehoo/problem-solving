from itertools import accumulate

N = int(input())
nums = list(map(int, input().split()))
T = int(input())


# 1
# for _ in range(T):
#     s, e = map(int, input().split())
#     answer = sum(nums[s - 1: e])
#     print(answer)

# 2
# accumulate = [0] * N
# accumulate[0] = nums[0]
# for i in range(1, N):
#     accumulate[i] = nums[i] + accumulate[i - 1]
#
# for _ in range(T):
#     s, e = map(int, input().split())
#     if s == 1:
#         print(accumulate[e - 1])
#     else:
#         print(accumulate[e - 1] - accumulate[s - 2])


result = list(accumulate(nums))
for _ in range(T):
    s, e = map(int, input().split())
    if s == 1:
        print(result[e - 1])
    else:
        print(result[e - 1] - result[s - 2])
"""
5
10 20 30 40 50
5
1 3
2 4
3 5
1 5
4 4

차곡차곡 쌓아올린다 => 인덱스 4에는 1,2,3,4까지의 합을 누적합.
3 ~ 4 는 -> 3, 4 의 누적 합
answer : 4 누적합 빼기 2 누적합
 
 
"""
