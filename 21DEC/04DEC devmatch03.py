def calculateComplexity(part):
    global value_idx
    global value_dict
    part = list(part)
    if len(part) == 1:
        value_dict[part[0]] = 0
        return 0
    elif len(part) == 2:
        r, c = value_idx[part[0]]
        r_, c_ = value_idx[part[1]]
        total = abs(r - r_) + abs(c - c_)
        value_dict[''.join(part)] = total
        value_dict[''.join(part[::-1])] = total
        return total
    # else:
    #     print(part[0], ''.join((part[1:])))
    #     try:
    #         total_ = calculateComplexity(part[:-1]) + calculateComplexity(''.join((part[-1])))
    #         value_dict[''.join(part)] = total_
    #         value_dict[''.join(part[::-1])] = total_
    #
    #     except TypeError:
    #         pass
    #     return


def solution(s):
    keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'for '],
                ['p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'],
                ['l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']]

    global value_idx
    global value_dict
    value_idx = {}
    value_dict = {}

    for rdx, row in enumerate(keyboard):
        for cdx, c in enumerate(row):
            value_idx[c] = (rdx, cdx)

    part_set = set()
    N = len(s)
    for n in range(1, N + 1):
        for i in range(N):
            try:
                part = s[i: i + n]
                if part not in part_set:
                    # 이제 part 의 복잡도를 구해야지.
                    calculateComplexity(part)

                    part_set.add(s[i: i + n])

            except IndexError:
                pass

    print(value_dict)


print(solution("abcc"))
# 부분 문자열 조합도 만들어야하고, => 딕셔너리로 저장해버리자. 같은 부분문자열 발생할 수 있으니. 
# 모든 부분문자열은 어떻게 만들것인가. 문자열 길이 우선 구하고. for i in range(0, N): i 만큼 슬라이싱
# 문자열간 거리 계산도 해야한다.
# 키보드 형태의 배열도 만들어야한다아님?
