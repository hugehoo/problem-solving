from collections import deque

a, b = map(int, input().split())

t = 0
roots = [0, [a]]
current = a
queue = deque()
queue.append(roots)

while queue:
    route = queue.popleft()
    if route[1][-1] == b:
        print(route[0])
        print(*route[1])
        break

    curr = route[1][-1] - 1
    queue.append([route[0] + 1, route[1] + [curr]])

    curr = route[1][-1] + 1
    queue.append([route[0] + 1, route[1] + [curr]])

    curr = route[1][-1] * 2
    queue.append([route[0] + 1, route[1] + [curr]])
