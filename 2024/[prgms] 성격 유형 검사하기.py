def solution(survey, choices):
    score = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }
    result = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    for s, c in zip(survey, choices):
        s_split = list(s)
        if c < 4:
            result[s_split[0]] = result.setdefault(s_split[0], 0) + score[c]
        elif c == 4:
            pass
        else:
            result[s_split[1]] = result.setdefault(s_split[1], 0) + score[c]
    answer = ''
    for r in [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]:
        if result[r[0]] < result[r[1]]:
            answer += r[1]
        else:
            answer += r[0]
    
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
