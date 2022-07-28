from itertools import combinations

L, C = map(int, input().split())
arr = list(map(str, input().split()))
ori_arr = set(arr)

sets = {"a", "e", "i", "o", "u"}
mo = [a for a in arr if a in sets]
ja = [a for a in arr if a not in sets]
ja_temp = [k for k in combinations(ja, 2)]
result = set()
for m in mo:
    for j in ja_temp:
        kamo = {m, *j}
        k = ori_arr.difference(kamo)
        for d in combinations(k, L - len(kamo)):
            result.add(''.join(sorted([*d, *kamo])))
result = sorted(list(result))
for r in result:
    print(r)
"""
모음 최소 하나
자음 최소 두개

모음 하나, 자음 두개 를 고른 후에, 선택되지 않은 모든 문자들을 하나의 집합으로 몰아넣고 꺼내 넣자.
C 는 최소 3, 최대 15
"""
