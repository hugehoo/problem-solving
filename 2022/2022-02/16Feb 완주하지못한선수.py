def solution(participant, completion):
    part_dict = {}
    comp_dict = {}
    part_set = set()
    for p in participant:
        part_dict[p] = part_dict.get(p, 0) + 1
        part_set.add(p)
    for c in completion:
        comp_dict[c] = comp_dict.get(c, 0) + 1

    for p in part_set:
        if part_dict.get(p) != comp_dict.get(p):
            return p


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))