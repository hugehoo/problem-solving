from collections import defaultdict


def solution(logs):
    no_dict = defaultdict(list)
    final_dict = defaultdict(list)
    answer = set()
    for log in logs:
        no, num, score = log.split(" ")
        no_dict[no].append((int(num), int(score)))

    for k, list_ in no_dict.items():
        if len(list_) >= 5:
            score_list = [0] * 101
            for l in list_:
                score_list[l[0]] = l[1]
            final_dict[k].append(score_list)

    temp = sorted(final_dict.items(), key=lambda x: x[1])
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if temp[i][1] == temp[j][1]:
                answer.add(temp[i][0])
                answer.add(temp[j][0])
    if len(answer) == 0:
        return ['None']
    return sorted(list(answer))



""" 

최대 힙 -> pop a 만큼 감소
나머지는 b 만큼 감소 -> how ?

"""
print(solution(
    ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90",
     "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]))
print(solution(["1901 10 50", "1909 10 50"]))
print(solution(["0001 1 0", "0001 2 0", "0001 3 0", "0001 4 0", "0001 5 0", "0456 1 0", "0456 2 0", "0456 3 0", "0456 4 0", "0456 5 0"]))
