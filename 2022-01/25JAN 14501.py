N = int(input())
data = []
for i in range(N):
    p, t = map(int, input().split())
    data.append((p, t))
for i in range(N):
    while True:
        p, t = data[i]

        p, t = data[t + i]

    # p, t = data[i]
print(data)