N = int(input())
board = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[2], reverse=True)
nation = {}
count = 0
for a, b, c in board:
    nation[a] = nation.get(a, 0) + 1
    if nation[a] == 3:
        nation[a] = 2
        continue
    else:
        print(a, b)
        count += 1
        if count == 3:
            exit(0)

"""
국가번호는 1부터 차례대로,
선수번호도 1부터 차례대로

9
1 1 230
1 2 210
1 3 205
2 1 100
2 2 150
3 1 175
3 2 190
3 3 180
3 4 195
"""
