def solution(gems):
    answer = []
    shortest = len(gems) + 1
    start_p, end_p = 0, 0
    check_len = len(set(gems))
    contained = {}
    while end_p < len(gems):
        if gems[end_p] not in contained:
            contained[gems[end_p]] = 1
        else:
            contained[gems[end_p]] += 1

        end_p += 1
        if len(contained) == check_len:  # 현재 구간내 모든 보석이 있을 때
            while start_p < end_p:
                if contained[gems[start_p]] > 1:
                    contained[gems[start_p]] -= 1
                    start_p += 1
                elif shortest > end_p - start_p:
                    shortest = end_p - start_p
                    answer = [start_p + 1, end_p]
                    break
                else:
                    break
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
