from sys import stdin
import heapq as q

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    res = []
    end_time_heap = []
    for _ in range(N):
        s, e, = map(int, input().split())
        res.append((s, e))
    res.sort()
    q.heappush(end_time_heap, res[0][1])
    for i in range(1, N):
        start_time = res[i][0]
        end_time = res[i][1]
        if end_time_heap[0] > start_time:
            q.heappush(end_time_heap, end_time)
        else:
            q.heappop(end_time_heap)
            q.heappush(end_time_heap, end_time)
    print(len(end_time_heap))
    
        

"""
4
1 3
2 4
3 5
4 6
"""
