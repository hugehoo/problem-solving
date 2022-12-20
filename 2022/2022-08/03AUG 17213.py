N = int(input())
R = int(input())
mo = 1
for i in range(1, R + N):
    mo *= i

za = 1
for j in range(1, R + 1):
    za *= j
for j in range(1, N):
    za *= j
print(int(za / mo))

"""
N 가지 만큼 무수히 많다. 
M 개를 고른다. 
1 , 1 , 1
나머지 7개는 -> 
"""
