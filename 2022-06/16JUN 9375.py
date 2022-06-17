from collections import Counter
import sys
input = sys.stdin.readline

if __name__ == "__main__":

    t = int(input())

    for i in range(t):
        n = int(input())
        wear = []
        for j in range(n):
            a, b = input().split()
            wear.append(b)

        wear_Counter = Counter(wear)
        print(wear_Counter)
        cnt = 1  # 각 종류마다 항목의 개수

        for key in wear_Counter:
            cnt *= wear_Counter[key] + 1

        print(cnt - 1)
