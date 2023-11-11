def solution(servers, sticky, requests):
    answer = [[] for i in range(servers)]
    len_request = len(requests)
    l = 0
    sequence = 0
    traffic_record = {}
    while len_request > l:
        traffic_id = requests[l]
        if traffic_id in traffic_record.keys():
            num = traffic_record.get(traffic_id)
            answer[num].append(traffic_id)
            sequence = num
        else:
            answer[sequence].append(traffic_id)
            traffic_record[traffic_id] = sequence
        sequence += 1
        if sequence >= servers:
            sequence = 0
        l += 1
    return answer


print(solution(2, False, [1, 2, 3, 4]))
print(solution(2, True, [1, 1, 2, 2]))
print(solution(2, True, [1, 2, 2, 3, 4, 1]))  # [1,3,1],[2,2,4]
#

"""
servers : 3 -> 0,1,2 / 3,4,5 / 6,7,8
servers : 3 -> 0,1,2 / 0,1,2, / 0,1,2
"""