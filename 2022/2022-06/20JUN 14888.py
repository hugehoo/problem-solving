import sys
from itertools import combinations

input = sys.stdin.readline


def team_point(team):
    point = 0
    for i in team:
        for j in team:
            point += s[i - 1][j - 1]
    return point


if __name__ == "__main__":
    n = int(input())
    s = [[0] * n for i in range(n)]
    for i in range(n):
        s[i] = list(map(int, input().split()))
    team1 = [0] * n
    team2 = [0] * n

    answers = []

    all = list(combinations(range(1, n + 1), n // 2))

    for i in range(len(all) // 2):
        team1 = all[i]
        team2 = all[len(all) - 1 - i]
        answers.append((abs(team_point(team1) - team_point(team2))))
    print(min(answers))

