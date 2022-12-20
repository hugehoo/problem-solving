N = int(input())
for _ in range(N):
    line = list(input())
    result = 0
    count = 0
    for l in line:
        if l == 'O':
            count += 1
        else:
            count = 0
        result += count
    print(result)



"""
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
"""