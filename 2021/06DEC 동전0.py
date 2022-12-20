N, K = map(int, input().split())
count = 0
coin_list = list()
for i in range(N):
    coin_list.append(int(input()))
for i in reversed(coin_list):
    count += K // i
    K %= i
print(count)


"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""