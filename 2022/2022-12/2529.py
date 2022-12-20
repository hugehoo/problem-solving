from itertools import permutations

k = int(input())
a = input().split()
small = [i for i in range(k + 1)]
big = [9 - i for i in range(k + 1)]

result = []
perms = permutations([i for i in range(10)], k + 1)
for per in perms:
    flag = True
    for i in range(len(a)):
        if a[i] == "<":
            if per[i] < per[i + 1]:
                continue
            else:
                flag = False
                break
        else:
            if per[i] > per[i + 1]:
                continue
            else:
                flag = False
                break
    if flag:
        result.append(per)
print(''.join(map(str, list(max(result)))))
print(''.join(map(str, list(min(result)))))

"""
2
< >
"""