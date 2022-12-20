N, K = map(int, input().split())

added_bottle = 0

while bin(N).count('1') > K:
    N += 1
    added_bottle += 1


# while bin(N).count('1') > K:
#     idx = bin(N)[::-1].index('1')  # N 에서 1이 처음 나타난 index 를 구하기 위해 거꾸로 뒤집는다.
#     bi_to_decimal = 2 ** idx  # 해당 인덱스(이진수)를 10진수로 변환
#     print(idx, bi_to_decimal, N)
#     added_bottle += bi_to_decimal
#     N += bi_to_decimal

print(added_bottle)