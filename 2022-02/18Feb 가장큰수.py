from collections import defaultdict


def solution(numbers):
    num_dict = defaultdict(list)
    for a in numbers:
        num_dict[str(a)[0]].append((str(a), a))
    temp = sorted(num_dict.keys(), reverse=True)
    result = ''
    for t in temp:
        num_dict[t].sort(key=lambda x: (x[0][0],x[0][-1],), reverse=True)
        for i in num_dict[t]:
            # print(i)
            result += str(i[1])

    return result


print(solution([3, 30, 34, 5, 9]))
# print(solution([3, 30, 54, 50, 21, 23, 2104]))
"""
[3, 30, 34, 5, 9]	
"""
