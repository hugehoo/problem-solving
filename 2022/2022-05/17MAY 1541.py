import sys

input = sys.stdin.readline

m = input().strip()
split_minus = m.split("-")
final = []
for s in split_minus:
    split_plus = s.split("+")
    # plus 로 나뉘었으면, 더해야지. 안나뉘면 놔두고
    semi_total = 0
    for p in split_plus:
        semi_total += int(p)
    final.append(semi_total)

# final 의 숫자들은 각각 빼야하는 것.
first = final[0]
for f in final[1:]:
    first -= f
print(first)




"""
55-50+40

10+20+30+40

00009-00009
"""
