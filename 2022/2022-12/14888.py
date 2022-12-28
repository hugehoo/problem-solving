N = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_v = -int(1e9)
min_v = int(1e9)


def dfs(depth, num, add, sub, mul, div):
    global max_v
    global min_v

    if depth == N:
        max_v = max(max_v, num)
        min_v = min(min_v, num)
    else:
        if add:
            dfs(depth + 1, num + data[depth], add - 1, sub, mul, div)
        if sub:
            dfs(depth + 1, num - data[depth], add, sub - 1, mul, div)
        if mul:
            dfs(depth + 1, num * data[depth], add, sub, mul - 1, div)
        if div:
            dfs(depth + 1, int(num / data[depth]), add, sub, mul, div - 1)


dfs(1, data[0], add, sub, mul, div)
print(max_v)
print(min_v)
