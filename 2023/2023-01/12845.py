N = int(input())
cards = sorted(list(map(int, input().split())), reverse=True)

result = [(cards[0] + card) for idx, card in enumerate(cards) if idx > 0]
print(sum(result))

"""
3
40 30 30
"""
