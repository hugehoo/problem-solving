from bisect import bisect_left

input()

base_dict = dict.fromkeys(map(int, input().split()), 0)
lis = []

for key, value in enumerate(map(int, input().split())):
    base_dict[value] = key
# base_dict 는 2 번째 input 의 문자를 key, index 를 value 로 갖는 dictionary 가 된다.

for key, value in base_dict.items():
    find = bisect_left(lis, value)
    if len(lis) == find:  # 위의 value 값이 lis 에 없다는 의미 ( = lis 의 최대 값보다 크다)
        lis.append(value)  # 그래서 lis 에는 value 값을 푸시
    else:
        lis[find] = value

print(len(lis))



