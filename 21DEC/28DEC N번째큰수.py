import sys
import heapq

read = sys.stdin.readline
N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
heap = []
for i in range(N):
    heapq.heappush(heap, (-board[N - 1][i], board[N - 1][i], N - 1, i))

count = 1
while heap:
    idx, first_value, first_row, first_col = heapq.heappop(heap)
    above_value = board[first_row - 1][first_col]
    # above_value 와 second_value 비교할 것
    s_idx, second_value, second_row, second_col = heapq.heappop(heap)
    if above_value < second_value:
        count += 1

    while above_value >= second_value:


"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
"""