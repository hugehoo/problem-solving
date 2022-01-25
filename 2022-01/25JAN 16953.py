from collections import deque

a, target = map(int, input().split())
queue = deque()
count = 0

queue.append((a * 2, 1))
queue.append((int(str(a) + '1'), 1))

while queue:
    num, count = queue.popleft()
    if num == target:
        print(count + 1)
        exit()
    elif num > target:
        continue
    else:
        queue.append((num * 2, count + 1))
        queue.append((int(str(num) + '1'), count + 1))
print(-1)
