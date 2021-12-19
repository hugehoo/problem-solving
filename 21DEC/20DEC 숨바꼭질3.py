

# def bfs(queue):
#     n, t = queue.popleft()
#     queue.append((n * 2, t))
#     for i in range(2):
#         n = n + move[i]
#         queue.append((n, t + 1,))
#     while queue:
#         n, t = queue.popleft()
#         if n == K:
#             print(t)
#             exit()
#         for idx, i in enumerate([2 * n, n - 1, n + 1]):
#             if 0 <= i < 100001:
#
#                 if idx == 0:
#                     if i == K:
#                         print(t)
#                         exit()
#                     queue.append((i, t))
#                 else:
#                     if i == K:
#                         print(t + 1)
#                         exit()
#                     queue.append((i, t + 1))
#
#
# N, K = map(int, input().split())
# move = [-1, 1, 2]
# queue = deque()
# queue.append((N, 0))
# bfs(queue)


from collections import deque


N, K = map(int, input().split())
MAX = 100001
arr = [-1] * MAX
arr[N] = 0
queue = deque()
queue.append(N)

while queue:
    n = queue.popleft()
    if n == K:
        print(arr[K])
        break
    for i in ([n * 2, n - 1, n + 1]):
        if 0 <= i < MAX and arr[i] == -1:
            if i == n * 2:
                arr[i] = arr[n]
                queue.append(i)

            else:
                arr[i] = arr[n] + 1
                queue.append(i)

"""
5 17

순간이동 후, 1씩 이동한다.
그냥 1씩 이동한다.
queue 에 위의 각 케이스를 하나씩 넣고 while 문 돌리면 어떤가

"""
