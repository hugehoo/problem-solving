def solution(alp, cop, problems):
    alp_max = 0
    cop_max = 0
    time = 0
    for p in problems:
        alp_max = max(alp_max, p[0])
        cop_max = max(cop_max, p[1])
    temp = sorted(problems, key=lambda x: (x[0] + x[1]))
    for i in range(len(temp) - 1):
        pops = temp[i]
        # print("pops ", pops)
        while alp < alp_max and cop < cop_max:
            print("0. ", alp, cop, pops)
            if alp >= pops[0] and cop >= pops[1]:
                next_pops = temp[i + 1]
                value = min(next_pops[0] - alp, next_pops[1] - cop)
                if value == 0:
                    value = max(next_pops[0] - alp, next_pops[1] - cop)

                if next_pops[0] - alp > next_pops[1] - cop:
                    time += ((value // pops[3]) * pops[4])
                    cop += ((value // pops[3]) * pops[3])
                    alp += (value // pops[3]) * pops[2]
                    # print("-", alp, cop)
                else:
                    time += ((value // pops[2]) * pops[4])
                    alp += ((value // pops[2]) * pops[2])
                    # print((value // pops[2]) , pops[3])
                    cop += (value // pops[2]) * pops[3]
                    # print("+ ", alp, cop, value)
                break
            # 앞 문제만 못 푸는 상태 = 뒷 문제는 풀 수 있다 -> 앞의 점수를 올린다.
            if alp < pops[0]:
                diff1 = (pops[0] - alp)
                time += diff1
                alp += diff1

            # 뒷 문제만 못 푸는 상태 = 앞 문제는 풀 수 있다 -> 뒤의 점수를 올린다.
            if cop < pops[1]:
                diff2 = (pops[1] - cop)
                time += diff2
                cop += diff2
    return time


""" 
모든 문제를 풀 필요는 없다. 그냥 한 시간씩 투자하여 각 능력을 키워도 된다.
최소의 코스트로 능력을 키워, 리미트를 넘어야한다.
적은 코스트 대비 높은 증가량을 가진 문제를 정렬 -> 
"""

# print(solution(10, 10,
#                [[10, 15, 2, 1, 2],
#                 [20, 20, 3, 3, 4]]
#                ))

print(solution(0, 0, [
    [0, 0, 2, 1, 2],
    [4, 5, 3, 1, 2],
    [4, 11, 4, 0, 2],
    [10, 4, 0, 4, 2]]
               ))
