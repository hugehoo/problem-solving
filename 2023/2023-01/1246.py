N, M = map(int, input().split())
price = [int(input()) for _ in range(M)]
price.sort()
max_price = 0
answer_idx = 0
for idx in range(M):
    if N >= len(price[idx:]):
        if price[idx] * len(price[idx:]) > max_price:
            max_price = price[idx] * len(price[idx:])
            answer_idx = price[idx]

print(answer_idx, max_price)
