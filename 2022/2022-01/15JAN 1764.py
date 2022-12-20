N, M = map(int, input().split())

a_set = set()
b_set = set()

for _ in range(N):
    a_set.add(input())
for _ in range(M):
    b_set.add(input())
result = sorted(a_set & b_set)
print(len(result))
for i in result:
    print(i)



