target = int(input())
ans = abs(100 - target)
M = int(input())
if M:
    # arr = set(list(map(int, input().split())))
    arr = set(input().split()) # tlqkf , int 로 매핑해서 답이 다르게 나온것임
else:
    arr = set()

for num in range(1000001):
    for n in str(num):
        if n in arr:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))
print(ans)
