import sys

input = sys.stdin.readline

N = int(input().rstrip())
students = {}
ans = [[-1, -1] for _ in range(4)]

for i in range(N):
    number, A, B, C, D = map(int, input().split())
    score = [A, B, C, D]
    students[number] = score

# 점수 비교, 국어부터
for i in range(4):
    for student in students:
        if ans[i][1] < students[student][i]:
            ans[i][0] = student
            ans[i][1] = students[student][i]
        if ans[i][1] == students[student][i]:
            ans[i][0] = min(student, ans[i][0])

    # 한번 상을 받은 친구는 없애준다.
    del (students[ans[i][0]])
for i in range(4):
    print(ans[i][0], end=" ")
