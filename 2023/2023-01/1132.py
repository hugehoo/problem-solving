N = int(input())
number_position = [[0, False] for _ in range(10)]
answer = 0

for _ in range(N):
    word = input()
    number_position[ord(word[0]) - 65][1] = True
    m = 1
    for idx in range(len(word) -1, -1, -1):
        number_position[ord(word[idx]) - 65][0] += m
        m *= 10
number_position.sort(reverse=True)

if number_position[9][1]: # if last frequnt number was in first place
    for i in range(8, -1, -1):
        if not number_position[i][1]: # 마지막부터 순회 ->  false 이면 없애도 된다.
            del number_position[i]
            break

for i in range(9):
    answer += (number_position[i][0] * (9 - i))
print(answer)





# for _ in range(N):
#     word = input()
#     m = 1
#     number_position[ord(word[0]) - 65][1] = True
#     for idx in range(len(word) - 1, -1, -1):
#         number_position[ord(word[idx]) - 65][0] += m
#         m *= 10
# number_position.sort(reverse=True)
# print(number_position)  # 각 알파벳이 어떤 자리에 얼마만큼 나왔는지 표시
#
# if number_position[9][1]:
#     for i in range(8, -1, -1):
#         if not number_position[i][1]:
#             del number_position[i]
#             break
#
# for i in range(9):
#     ans += (number_position[i][0] * (9 - i))
# print(ans)
"""
2
ABC
BCA

1875

1
ABCDEFGHIJ

9876543210


2
ABCDEFGHIJ
J

9876543202


10
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
AJJJJJJJJJ

9973936905


5
GHJIDDD
AHHCCCA
IIJCEJ
F
HDBIGFJAAJ

9888114550
"""