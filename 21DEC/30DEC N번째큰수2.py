import sys
import heapq

read = sys.stdin.readline
N = int(read())
heap = []
for _ in range(N):
    nums = list(map(int, read().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
            print("num", num)
    else:
        for num in nums:
            if heap[0] < num:
                print(num, heap[0], heap)
                heapq.heappush(heap, num)
                heapq.heappop(heap)
print(heap[0])



"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
"""
