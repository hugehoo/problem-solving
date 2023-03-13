n = int(input())
direction = list(input())
r, c = 1, 0
s_r, s_c = 49, 49
map_ = [['#' for _ in range(100)] for _ in range(100)]
map_[s_r][s_c] = "."
current_status = 'south'
temp = [[s_r, s_c]]
min_r, max_c = 100, 100
for d in direction:
    min_r = min(s_r, min_r)
    max_c = min(s_c, max_c)
    if d == 'F':
        if current_status == 'south':
            s_r += 1
            map_[s_r][s_c] = '.'
        elif current_status == 'west':
            s_c -= 1
            map_[s_r][s_c] = '.'
        elif current_status == 'east':
            s_c += 1
            map_[s_r][s_c] = '.'
        elif current_status == 'north':
            s_r -= 1
            map_[s_r][s_c] = '.'
    elif d == 'L':
        if current_status == 'south':
            current_status = 'east'
        elif current_status == 'west':
            current_status = 'south'
        elif current_status == 'east':
            current_status = 'north'
        elif current_status == 'north':
            current_status = 'west'
    else:
        if current_status == 'south':
            current_status = 'west'
        elif current_status == 'west':
            current_status = 'north'
        elif current_status == 'east':
            current_status = 'south'
        elif current_status == 'north':
            current_status = 'east'
    min_r = min(s_r, min_r)
    max_c = min(s_c, max_c)
    temp.append([s_r, s_c])
# for t in temp:
#     print(t)
# print("   ")
new_temp = [[r - min_r, c - max_c] for r, c, in temp]
new_R = max(list(map(lambda x: x[0], new_temp)))
new_C = max(list(map(lambda x: x[1], new_temp)))

pp = [['#'] * (new_C + 1) for _ in range(new_R + 1)]
for r, c in new_temp:
    pp[r][c] = '.'

for p in pp:
    print(''.join(p))
"""
0 0
0 1
0 2
0 2
1 2
2 2
...
##.
##.
...
##.
##.
"""
