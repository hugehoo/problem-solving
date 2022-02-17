def solution(n, lost, reserve):
    lost_dict = {}
    count = 0
    reserve_set = set(reserve)
    for l in lost:
        for ele in check_front_back(l, n):
            if ele in reserve_set:
                reserve_set.discard(ele)
                break
        else:
            count += 1
    return n - count


def check_front_back(m, n):
    if m - 1 == 0:
        return [m + 1]
    elif m + 1 > n:
        return [m - 1]
    if m - 1 > 0 and m + 1 <= n:
        return [m - 1, m + 1]


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
# reserve 에서 하나씩 꺼내면서 앞 뒤 비교.
# lost 에 해당 값 있으면 없애기.

# lost 순회하면서, 주변 사람 번호 캐싱
