# import sys
#
# input = sys.stdin.readline
#
# first = list(input().strip())
# second = list(input().strip())
#
# first = [0] + first
# second = [0] + second
# board = [[0] * (len(first)) for _ in range(len(second))]
#
# for sec in range(1, len(second)):
#     for fir in range(1, len(first)):
#         if first[fir] == second[sec]:
#             board[sec][fir] += (board[sec - 1][fir - 1] + 1)
#         else:
#             board[sec][fir] = max(board[sec - 1][fir], board[sec][fir - 1])
# answer = 0
# for b in board:
#     answer = max(max(b), answer)
# print(answer)

A, B = input(), input()

lcs_list = [0]*len(A) # 각 위치별 lcs 저장
for i in range(len(B)):
    until_lcs = 0
    for j in range(len(A)):
        now_lcs = lcs_list[j]
        if B[i] == A[j]:
            lcs_list[j] = until_lcs + 1
        if until_lcs < now_lcs:
            until_lcs = now_lcs
print(max(lcs_list))