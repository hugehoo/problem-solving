def solution(N, S):
    reserved_rows = {i: set() for i in range(1, N + 1)}
    
    seat_groups = [
        {'A', 'B', 'C'},
        {'D', 'E', 'F', 'G'},
        {'H', 'J', 'K'}
    ]
    
    family_sets = [
        {"B", "C", "D", "E", "F", "G", "H", "J"},
        {"D", "E", "F", "G"},
        {"B", "C", "D", "E"},
        {"F", "G", "H", "J"},
    ]
    if S:
        for seat in S.split():
            row = int(seat[:-1])
            column = seat[-1]
            reserved_rows[row].add(column)
    result = 0
    valid_families = []
    for rows in reserved_rows.values():
        if rows:
            for family in family_sets:
                if len(family) == 8:
                    if not rows & family:
                        result += 2
                        break
                elif len(family) == 4:
                    if not rows & family:
                        result += 1
                        break
        else:
            result += 2
    return result


# 테스트
print(solution(2, "1A 2F 1C"))  # 예상 출력: 2
# print(solution(1, ""))  # 예상 출력: 2
# print(solution(22, "1A 3C 2B 20G 5A"))  # 예상 출력: 41

"""
가능한 가족 row :
"""
