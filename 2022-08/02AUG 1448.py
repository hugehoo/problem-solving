n = int(input())
nums = sorted([int(input()) for _ in range(n)])
num_dict = {}
for num in nums:
    num_dict[num] = num_dict.get(num, 0) + 1
keys = sorted(num_dict.keys(), reverse=True)

for k in range(len(keys) - 1):
    for p in range(k + 1, len(keys)):
        try:
            if num_dict[keys[k]] > 1 and keys[k] < keys[k] + keys[p]:
                print(keys[p] + keys[k] * 2)
                exit()
            if num_dict[keys[p]] > 1 and keys[k] < keys[p] + keys[p]:
                print(keys[k] + keys[p] * 2)
                exit()
            elif num_dict[keys[p]] == 1 and keys[k] < keys[p] + keys[p + 1]:
                print(keys[k] + keys[p] + keys[p + 1])
                exit()
            else:
                break
        except IndexError:
            print(-1)
            exit()

"""
2 2 2 3 3 4
최대 100만개 까지 주어진다. 
combinations() 사용 불가. 
O(N^2) 불가

딕셔너리 -> 가장 큰거 와 나머지 두개의 합 비교. 

"""
