from sys import stdin

read = stdin.readline
M, N = map(int, read().split())
name_dict = {}
for _ in range(M):
    site, pswd = read().split()
    name_dict[site] = pswd
for _ in range(N):
    site = read().rstrip()
    print(name_dict[site])
