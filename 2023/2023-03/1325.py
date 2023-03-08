from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(set)
numbers = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].add(a)
    numbers[a] = set()
    numbers[b] = set()


def dfs(number, key):
    if not graph[number]:
        return
    
    for num in graph[number]:
        if num not in numbers[key] and num != key:
            numbers[key].add(num)
            dfs(num, key)
    return


for n in numbers:
    if graph[n]:
        for g in graph[n]:
            dfs(g, n)
            
a = list(map(lambda x: len(numbers[x]), numbers.keys()))
max_value = max(a)
result = sorted([key for key in numbers.keys() if max_value == len(numbers[key])])
print(*result)



