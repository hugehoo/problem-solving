import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    name_dict = {}
    for _ in range(N):
        name, msg = map(str, input().split())
        name_dict[name] = name_dict.get(name, 0) + 1
    answer = []
    for k in name_dict.keys():
        if name_dict.get(k) == 1:
            answer.append(k)
    answer.sort(reverse=True)
    for a in answer:
        print(a)



