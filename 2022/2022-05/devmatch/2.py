from collections import defaultdict


def solution(rooms, target):
    room_dict = dict()
    for r in rooms:
        num, name = r.split("]")
        names = name.split(',')
        num = int(num[1:])
        room_dict[num] = room_dict.get(num, names)
    filters = room_dict[target]
    for num in room_dict.keys():
        if num != target:
            for f in filters:
                if f in room_dict[num]:
                    room_dict[num].remove(f)
    room_dict.__delitem__(target)
    nominates = defaultdict()
    temp = defaultdict(list)
    for k, value in room_dict.items():
        for v in value:
            nominates[v] = nominates.get(v, 0) + 1
            temp[v].append(k)
    final = defaultdict(list)
    for k in nominates.keys():
        final[k] = [nominates[k], temp[k]]
    distance = defaultdict(list)
    for k in room_dict.keys():
        distance[k] = abs(target - k)
    for k, v in final.items():
        samp = []
        for p in final[k][1]:
            samp.append(distance[p])
        final[k][1] = sorted(samp)
    ff = sorted(final, key= lambda x : (final[x][0], final[x][1]), reverse=True)
    return ff[::-1]

    """
    target 을 키로 가진 밸류는 아예 삭제. 
    노미네이츠 각 인원마다 지정 자리 수 카운트 (dict)
    호수별 거리 계산 -> target 과의 거리만 알면 된다. 위의 딕트에 추가. 
    dict -> { name : [count, distance] }
    """


print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))
# print(solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202))
