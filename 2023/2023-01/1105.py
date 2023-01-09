L, R = map(str, input().split())
list_l = list(L)
list_r = list(R)
if len(list_l) != len(list_r):
    print(0)
    exit()

answer = 0
for idx in range(len(list_l)):
    if list_l[idx] == list_r[idx]:
        if list_l[idx] == '8':
            answer += 1
    else:
        break
print(answer)


"""
for문은 생각도 말고..
자리수로 접근
1 10 -> 0 : 즉 8이외의 수를 골라도 됨.
포문이라 치면, 순회하면서 8이 0개인 상태를 계속 카운팅하다, 8의 개수마다 min 을 업데이트.
근데 포문 안돼.

근데 R 이 20억이더라도, L 이 1이면, 답은 0임.
R 이 20억이고, L 이 10억이더라도, 답은 0임.
즉 L 에 8이 몇개냐에 따라 답이 결정된다.
L 부터는 커질 일만 있다.
 L 에 8이 없다면 답은 0이고, 8이 있다면, 그 개수보다 같거나 작아진다.
 if L.count(8) = min_count 으로 지정
 R - L = diff
 diff 가 1이라도 난다 -> L 의 1의 자리 숫자가 8이다.  min_count - 1 가능함.
 10의 자리 숫자가 8이다. 근데 차이가 10 미만이다. min_count 그대로 됨.
 즉 몇의 자리 숫자에 8이 있고, diff 가 그 수보다 크거나 같으면 차감된다.


"""
# diff = R - L
#
# str_L = str(L)
# min_count = str_L.count('8')
# N = len(str_L)
# dic = dict()
#
# if min_count == 0:
#     print(0)
#     exit()
#
# for idx, num in enumerate(str_L):
#     if num == '8':
#         dic[N - idx] = 1
#
# len_diff = len(str(diff))
# if diff == 0:
#     print(min_count)
#     exit()
# count = 0
# for key in dic.keys():
#     if len_diff < key:
#         count += 1
# print(count)
"""
L = 888
R = 1000
R = 999
R = 899
diff = 112
diff = 111
diff = 11
900
"""

