# # A, B, C = list(map(int, input().split()))
# #
# # print((10 ** 5) * (10 ** 5) * 10 % 12)
# def power(a, b):
#     if b == 1: # b의 값이 1이면 a % C를 return한다.
#         return a % C
#     else:
#         temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
#         if b % 2 == 0:
#             return temp * temp % C # b가 짝수인 경우
#         else:
#             return temp * temp * a % C # b가 홀수인 경우
#
#
# if __name__ == "__main__":
#     A, B, C = map(int, input().split())
#
#     result = power(A, B)
#     print(result)
# """
# 10 11 12
# """
