from itertools import product

a, b = map(int, input().split())
a_len = len(str(a))
b_len = len(str(b))
count = 0
for i in range(a_len, b_len + 1):
    for n in product([4, 7], repeat=i):
        join = ''.join(list(map(str, n)))
        if a <= int(join) <= b:
            count += 1
print(count)

"""
간단하게는 range(N, M + 1) 돌리면 되는데, 시간 오류 날듯 (10억)
10억은 10자리수
M 은 몇자리수 인지 파악
N 은 몇자리 수인지 파악 
(M 에서 나올 수 잇는 금민수 개수) - (N 에서의 금민수 개수)
1 10
11 20
74 77
1000000 5000000

앞자리수가 7 미만이면, 4만 올 수 있다. 
4 미만이면, 그 아랫자리부터 연산

케이스1
7보다 크거가 같다.

케이스 2
4보다 크고 7보다 작다

케이스 3
4보다 작다

662 -> 477, 447 ...

"""
