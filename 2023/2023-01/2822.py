num_dict = {}
i = 1
for _ in range(1, 9):
    num = int(input())
    num_dict[num] = i
    i += 1
num_list = sorted(num_dict.keys(), reverse=True)[:5]
print(sum(num_list))
result = sorted([num_dict[n] for n in num_list])
print(*result)
