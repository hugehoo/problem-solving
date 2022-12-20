scenario = 1

while True:
    N = int(input())

    if N == 0:
        break

    name_list = [input() for i in range(1, N + 1)]
    sample = [input().split()[0] for _ in range((2 * N - 1))]
    idx = [i for i in range(1, N + 1) if sample.count(str(i)) == 1]
    print(scenario, name_list[idx[0] - 1])
    scenario += 1

"""
3
Betty Boolean
Alison Addaway
Carrie Carryon
1 B
2 A
3 B
3 A
1 A
2
Helen Clark
Margaret Thatcher
1 B
2 B
2 A
0
"""
