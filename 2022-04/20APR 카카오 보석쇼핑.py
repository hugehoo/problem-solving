

def solution(gems):
    def containAll(param: list):
        gem_set = set(gems)
        for g in gem_set:
            if g not in param:
                return False
        else:
            return True

    sp, ep, = 0, 0
    N = len(gems)
    MAX_LENGTH = N
    answer = []
    if 1 == len(set(gems)):
        return [1, 1]

    for e in range(ep, N):
        for s in range(sp, e):
            if containAll(gems[s: e + 1]) and MAX_LENGTH >= e - s + 1:
                MAX_LENGTH = e - s + 1
                if answer and answer[-1][1] - answer[-1][0] > e - s:
                    answer.pop()
                    answer.append([s + 1, e + 1])
                else:
                    answer.append([s + 1, e + 1])
                sp += 1
        ep += 1
        # sp 는 언제 추가? -> if MAX_LENGTH 조건을 만족할 때
    answer.sort()
    return answer[0]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
