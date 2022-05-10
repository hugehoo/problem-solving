def solution(survey, choices):

    mbti_type = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    answer = []
    character_score = {}

    for s, c in zip(survey, choices):
        score = abs(4 - c)
        if 4 - c < 0:
            character_score[s[1]] = character_score.get(s[1], 0) + score
        elif 4 - c > 0:
            character_score[s[0]] = character_score.get(s[0], 0) + score
        else:
            continue

    for mbti in mbti_type:
        if character_score.get(mbti[0], 0) < character_score.get(mbti[1], 0):
            answer.append(mbti[1])
        else:
            answer.append(mbti[0])

    return ''.join(answer)


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
