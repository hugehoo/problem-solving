N, L = map(int, input().split())
location = list(map(int, input().split()))
location.sort()

start = 0
cnt = 0

for loc in location:
    if start < loc:
        start = loc + (L - 1)
        cnt += 1
print(cnt)

"""
4 2
1 2 100 101

테이프 길이는 변함없다.
핵심 -> 특정 시작점에서 테이프 길이만큼 붙인다면, (시작점 + 테이프) 보다 작은 지점에 대해선 생각할 필요 없다
"""
