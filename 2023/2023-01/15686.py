from itertools import combinations


N, M = map(int, input().split())
city, chickens, homes = [], [], []
ans = float("inf")

for n in range(N):
    line = list(map(int, input().split()))
    city.append(line)
    for ldx, l_ in enumerate(line):
        if l_ == 1:
            homes.append((n + 1, ldx + 1))
        elif l_ == 2:
            chickens.append((n + 1, ldx + 1))

for chicken in list(combinations(chickens, M)):
    sum_distance = 0
    for x1, y1 in homes:
        min_distance = float("inf")
        for x2, y2 in chicken:
            min_distance = min(min_distance, abs(x1 - x2) + abs(y1 - y2))
        sum_distance += min_distance
    ans = min(ans, sum_distance)
print(ans)

"""
M 최대는 13
치킨집 개수에서 M 만큼 고른다. 조합 사용
    1) M 과 치킨집 개수가 같다면 개꿀. 
    2) 
각 조합마다 치킨거리 연산.
집의 개수는 2N 을 넘지 않고, 최소 1개 존재. 
-> M <= 치킨집 수 <= 13

집의 좌표를 리스트에 저장. 
치킨집 좌표도 리스트에 저장. 
M 개만 꺼내씀.temp => 조합 생성
for h in house:
    for t in temp:
        h 와 t 거리 계산
        또 계산
        모아둠
    가장 작은거 출력해서 누적. 
"""
