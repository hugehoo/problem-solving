import sys

input = sys.stdin.readline
print(
4400+
24000+
5000+
10000+
116000+
36500+
59000
)
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]
i = 0
result = []
while N > i:
    x, y = arr[i]
    k = 1
    for idx, values in enumerate(arr):
        if idx == i:
            continue
        
        if values[0] > x and values[1] > y:
            k += 1
    i += 1
    result.append(str(k))
print(' '.join(result))


"""
5
55 185
58 183
88 186
60 175
46 155



이마트24 4400
버거킹 24000
주차비 5000
튜브 10000
평상 및 식사 116000
요아정 36500
그린카 59000


"""
