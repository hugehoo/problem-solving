N = int(input())

origin = [0] * (N + 1)
for i in range(1, N + 1):
    origin[i] = int(input())

count_arr = [0] * (N + 1)
for j in range(1, N + 1):
    visited = [j]
    count = 1
    num = origin[j]
    while num not in visited:
        visited.append(num)
        num = origin[num]
        count += 1
    count_arr[j] = count
print(count_arr.index(max(count_arr)))
