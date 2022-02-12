import sys

input = sys.stdin.readline
n, target_weight = map(int, input().split())
table = [0] * (target_weight + 1)
for _ in range(n):
    weight, value = map(int, input().split())
    if weight > target_weight:
        continue
    for j in range(target_weight, 0, -1):
        if j + weight <= target_weight and table[j] != 0:
            table[j + weight] = max(table[j + weight], table[j] + value)
    table[weight] = max(table[weight], value)
print(max(table))

"""
입력과 출력을 써놓고 시작하자. 
출력이 좀 더 중요함 -> 정답과 매칭되는 것이니.  
      w      v
A     6      13
B     4      8
c     3      6
d     5      12



4 7
6 13
4 8
3 6
5 12
"""