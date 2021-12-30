import sys
import heapq

read = sys.stdin.readline
N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
heap = []


def find_above(elem):
    new_N = elem[2] - 1
    col = elem[3]
    return [-board[new_N][col], board[new_N][col], new_N, col]


count = 0
for i in range(N):
    heapq.heappush(heap, (-board[N - 1][i], board[N - 1][i], N - 1, i))

pops = heapq.heappop(heap)
above = find_above(pops)
pops2 = heapq.heappop(heap)
count += 1

while True:
    if above[1] > pops2[1]:
        above = find_above(above)
        count += 1
        flag = 'above'
    else:
        above = find_above(pops2)
        pops2 = heapq.heappop(heap)
        count += 1
        flag = 'pops2'

    if count == N:
        if flag == 'above':
            print(above, 'above')
            break
        else:
            print(pops2, 'pops2')
            break

# count = 1
# while heap:
#     idx, first_value, first_row, first_col = heapq.heappop(heap)
#     above_value = board[first_row - 1][first_col]
#     # above_value 와 second_value 비교할 것
#     s_idx, second_value, second_row, second_col = heapq.heappop(heap)
#     if above_value < second_value:
#         count += 1
#
#     while above_value >= second_value:


"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
"""
