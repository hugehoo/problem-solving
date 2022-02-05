from collections import defaultdict
import sys
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())  # N : 사람의 수, M : 파티의 수
truth_total = set(map(int, input().split()[1:]))  # 진실을 아는 사람의 수와 번호
party_dict = defaultdict(list)

for m in range(M):
    party_dict[m] = list(map(int, input().split()[1:]))

flag = True
while flag:
    before = deepcopy(truth_total)
    for values in party_dict.values():
        if truth_total & set(values):

            # old
            # for v in values:
            #     truth_total.add(v)

            # new
            difference = set(values).difference(truth_total)
            truth_total.update(difference)
    after = truth_total
    if before == after:
        flag = False

count_ = 0
for k, v in party_dict.items():
    if set(v) & truth_total:
        continue
    else:
        count_ += 1
print(count_)


"""
4 5
1 1 3
1 1
1 2
1 3
2 4 2
2 4 1

4 1
0
0

5 5
1 3
1 1
2 1 2
2 1 3
2 1 4
2 1 5
// 0

6 5
1 6
2 4 5
2 1 2
2 2 3
2 3 4
2 5 6 
// 0
"""