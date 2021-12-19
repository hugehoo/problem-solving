N, C = map(int, input().split())
dict_num = {}

for elem in list(map(int, input().split())):
    dict_num[elem] = dict_num.get(elem, 0) + 1

li = sorted(dict_num.items(), key=lambda x: x[1], reverse=True)

print(' '.join(map(str, [k for k, v in li for _ in range(v)])))

# map을 해줘야 하는 이유, int < - > str

"""
횟수, 먼저 나온 순, 

5 2
2 1 2 1 2

9 3
1 3 3 3 2 2 2 1 1

9 77
11 33 11 77 54 11 25 25 33
"""
