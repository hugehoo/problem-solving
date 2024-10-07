import sys

input = sys.stdin.readline

K, N = map(int, input().split())
numbers = [int(input()) for _ in range(K)]
start, end = 1, max(numbers)


def get_lines():
    line = 0
    for i in numbers:
        line += i // mid
    return line


while start <= end:
    mid = (start + end) // 2
    if get_lines() >= N:  # 필요한 랜선 수 N 보다 자른 랜선 수가 더 많을 때 => 자른 길이를 더 늘려도 된다.
        start = mid + 1  # 그래서 랜선의 start 를 mid + 1 로 올려줌
    else:
        end = mid - 1
print(end)

"""
많이 만드는 것도 포함됨
만들 수 있는 최대 랜선 길이

450 530 740 800
2    2   3   4
가장 작은 랜선 보단 항상 같거나 작겠네.
210 일 경우 -> 420 420 630 840

그리디 -> 다 해본다.
최대 만개 가질 수 있고, 최대 100만 개까지 만들어야 한다.
231 로도 만들수 있는데, 200으로도 만들수있다.
231 이 오답인 이유는 , 231로는 11개를 만들 수 없기 때문.


for i in range(231, 0):
    for j in inputs
    break
"""
