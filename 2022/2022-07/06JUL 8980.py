import sys
from collections import defaultdict
input = sys.stdin.readline

N, C = map(int, input().split())
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
arr.sort(key=lambda x : x[1])
print(arr)

"""
배송할 수 있는 최대 박스 수
마을 수 , 택배차 용량

4 40
6
3 4 20
1 2 10
1 3 20
1 4 30
2 3 10
2 4 20
"""
