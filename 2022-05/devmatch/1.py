def dust(number):
    if number >= 151:
        return "REALLY_BAD"
    elif 150 >= number >= 81:
        return "BAD"
    elif 80 >= number >= 31:
        return "NORMAL"
    else:
        return "GOOD"


def micro(number):
    if number >= 76:
        return "REALLY_BAD"
    elif 75 >= number >= 36:
        return "BAD"
    elif 35 >= number >= 16:
        return "NORMAL"
    else:
        return "GOOD"


def new_mask():
    return [True, 0]


def solution(atmos):
    mask_on = ["REALLY_BAD", "BAD"]
    mask_count = 0
    mask_day = 0  # 사용일부터 1
    for d, m, in atmos:
        dust_result = dust(d)
        micro_result = micro(m)
        if dust_result == "REALLY_BAD" and micro_result == "REALLY_BAD":
            if mask_day == 0:
                mask_count += 1
            mask_day = 0
            # 이미 마스크를 끼고 있는데, 이틀 전이라면 그대로 쓰면 된다. -> 그리고 버리면 된다.
            # 근데 마스크가 없다면 무조건 새로 끼고 버려야한다.
            # 공통된 로직은 마스크를 끼고, 버린다.
            # 차이점은 마스크가 없다면, 새로 마스크를 생성하고, 이미 마스크가 있다면 새로 생성할 필요가 없다는 점
            continue
        if dust_result in mask_on or micro_result in mask_on:
            if mask_day == 0:
                mask_count += 1
                mask_day += 1
                continue
            else:
                if mask_day >= 3:
                    mask_day = 0
                    continue
                else:
                    mask_day += 1
                    if mask_day == 3:
                        mask_day = 0
        else:
            if mask_day > 0:
                mask_day += 1
                if mask_day == 3:
                    mask_day = 0

        # if mask_day > 0:
        #     mask_day += 1
        # if mask_day > 3:
        #     mask_day = 0


    return mask_count


"""
마스크 재사용 가능
이틀 후 까지만 재사용 가능
-> 둘다 매우 나쁨이면 사용 X

필요한 마스크 갯수
"""

print(solution([[80, 35], [70, 38], [100, 41], [75, 30], [160, 80], [77, 29], [181, 68], [151, 76]]))
print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]))
print(solution([[30, 15], [80, 35]]))
