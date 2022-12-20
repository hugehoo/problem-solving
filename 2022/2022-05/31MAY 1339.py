import sys

input = sys.stdin.readline

N = int(input())
arrays = sorted([input().strip() for _ in range(N)], key=lambda x: (len(x), x), reverse=True)
print(arrays)
M = len(arrays[0])
new_arrays, alphabet_hash = [], {}
num = [i for i in range(0, 10)]

for idx, o in enumerate(arrays):
    if len(o) < M:
        o = "-" * (M - len(o)) + o
        new_arrays.append(list(o))
        continue
    new_arrays.append(list(o))

for k in zip(*new_arrays):
    for z in k:
        if z != "-" and alphabet_hash.get(z, 0) == 0:
            alphabet_hash[z] = num.pop()
answer = 0
for a in arrays:
    temp = ''
    for a_ in a:
        temp += str(alphabet_hash[a_])
    answer += int(temp)
print(answer)

