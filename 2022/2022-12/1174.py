from itertools import combinations


N = int(input())
result = set()

# 1
for i in range(1, 11):
    for com in combinations(range(0, 10), i):
        com = sorted(com, reverse=True)
        result.add(int(''.join(map(str, com))))
result = sorted(result)

try:
    print(result[N - 1])
except IndexError:
    print(-1)

# 2
number = []


def dfs():
    if number:
        result.add(int(''.join(map(str, number))))
    for i in range(10):
        if not number or number[-1] > i:  # 왼쪽 수가 오른쪽 수 보다 크므로 감소 케이스
            number.append(i)
            dfs()
            number.pop()


dfs()
result = sorted(result)
print(result[N - 1] if len(result) >= N else -1)



"""
1자리 수 0 ~ 9 
2자리 수 10 ~ 90 : 앞자리 수만큼 케이스 생김 ex) 9x : 9가지
3자리 수 210 ~ 987 : 맨 앞자리 수(k) 보다 작은 경우, k - 1 가지 

1xx : 1 : 1
3xx : 2 + 1 : 3 
4xx : 3 + 2 + 1 : 6 
5xx : 4 + 3 + 2 + 1 : 10
"""
# def sample(k: int):
#     if len(set(str(k))) == len(str(k)) and str(i) == ''.join(sorted(list(str(i)), reverse=True)):
#         return True
#
#
# res = 0
# while True:
#     # if count > int(N):
#     #     res = -1
#     if i == 1000000:
#         print(-1)
#         exit()
#     if count == int(N):
#         break
#     if sample(i):
#         res = i
#         count += 1
#     i += 1
# print(res)