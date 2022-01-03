l1, l2 = [], []
for _ in range(3):
    X, Y = map(int, input().split())
    l1.append(X)
    l2.append(Y)

for i, j in zip(l1, l2):
    if l1.count(i) == 1: x = i
    if l2.count(j) == 1: y = j

print(x, y)




"""
5 5
5 7
7 5
"""