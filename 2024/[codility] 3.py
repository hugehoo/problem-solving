def solution(N, S):
    # 가능한 가족 좌석 집합
    family_sets = [
        frozenset(["B", "C", "D", "E"]),
        frozenset(["F", "G", "H", "J"]),
        frozenset(["D", "E", "F", "G"])
    ]
    
    # 각 행별로 예약된 좌석 정리
    rows = {}
    if S:  # S가 비어있지 않은 경우에만 처리
        for seat in S.split():
            row = int(seat[:-1])
            column = seat[-1]
            if row not in rows:
                rows[row] = set()
            rows[row].add(column)
    
    total_families = 0
    
    for row in range(1, N + 1):
        reserved = rows.get(row, set())
        
        # 중앙 좌석 (DEFG)가 비어있는지 확인
        if not reserved & family_sets[2]:
            total_families += 1
            continue
        
        # 왼쪽 (BCDE)와 오른쪽 (FGHJ) 좌석 확인
        left_available = not reserved & family_sets[0]
        right_available = not reserved & family_sets[1]
        
        if left_available and right_available:
            total_families += 2
        elif left_available or right_available:
            total_families += 1
    
    return total_families


# 테스트
test_cases = [
    (2, "1A 2F 1C"),
    # (4, "1A 1B 1C 2D 2F 2G 2H 3A 3K"),
    # (3, ""),
    # (5, "1A 2A 3A 4A 5A 1K 2K 3K 4K 5K"),
    (22, "1A 3C 2B 20G 5A")
]

for i, (N, S) in enumerate(test_cases, 1):
    result = solution(N, S)
    print(f"행 수: {N}")
    print(f"예약된 좌석: {S}")
    print(f"최대 가족 수: {result}\n")
# def solution(N, S):
#     reserved_rows = {i: set() for i in range(1, N + 1)}
#
#     if S:
#         for seat in S.split():
#             row = int(seat[:-1])
#             column = seat[-1]
#             reserved_rows[row].add(column)
#     two_family_case = {'A', 'K'}
#     result = 0
#     for n in range(1, N + 1):
#         reserved_seats = reserved_rows[n]
#         if reserved_seats:
#             if len(reserved_seats) == 1:
#                 if 'A' in reserved_seats or 'K' in reserved_seats:
#                     result += 2
#                 else:
#                     result += 1
#             if len(reserved_seats) == 2:
#                 print(reserved_seats)
#                 if 'A' in reserved_seats and 'K' in reserved_seats:
#                     result += 2
#                 elif reserved_seats <= {'D', 'E', 'F', 'G'}:
#                     pass
#                 else:
#
#
#
#         else:
#             result += 2
#
#     print(result)
#     return reserved_rows
#
#
# # 테스트
# result = solution(13, "3A 3D 4A 5D 5E 6C 1K 13A")
# print(result)
#
# """
#
#
# 우선 같은 줄에 예약된 좌석끼리 묶어야함.
# 그래서 한줄 씩 확인 ->
# 예약석이 3개 이상이면 최대 1가족.
# 근데 3개일때 안되는경우 -> 각 한묶음씩 앉는 경우
# 시트별 묶음을 만들 시 -> {a,b,c}, {d,e,f,g}, {h,j,k}
#
# 예약 2석일 때 -> 2가족인 경우 : a,k. 이외에는 무조건 한 가족
# 예약 1석일 때 -> 2가족인 경우 : a or k 일 때. 그 외에는 무조건 한 가족.
# 한 로우씩 포문 순회하면서 verify() 함수를 만들자.
#
# 한줄에는 최대 2가족이 앉을 수 있다.
# N = 22, 1a, 3c, 2b, 20g, 5a
# 1  a
# 2    b
# 3      c
# 5  a
# 20            g
# 44 -> 3줄은 한가족밖에 안됨
#
# 22 - 5 = 17 * 2 = 34 가족
# 1a -> 2
# 2b  -> 1
# 3c -> 1
# 5a -> 2
# 20g -> 1
# """
