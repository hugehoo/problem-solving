from collections import defaultdict


def solution(id_list, report, k):
    mail_dict = {}
    report_dict = defaultdict(set)
    result = []

    for one in report:
        content = one.split(" ")
        report_dict[content[1]].add(content[0])
    for key, value in report_dict.items():
        if len(value) >= k:
            for v in value:
                mail_dict[v] = mail_dict.get(v, 0) + 1
    for id_ in id_list:
        result.append(mail_dict.get(id_, 0))
    return result


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# print(solution([[0, 3], [1, 9], [2, 6]]))
