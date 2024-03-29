C, N = map(int, input().split())
result = [list(map(int, input().split())) for _ in range(N)]
# 여기 정렬 칠 때, 비율이 같은 것에 대해서는 어떻게 해야하나?
result = sorted(result, key=lambda x: (x[1] / x[0], x[0]), reverse=True)
print(result)
# base, remain = divmod(C, result[0][1])
# answer = base * result[0][0]
#
# if not remain:
#     print(answer)
# else:
#     min_value = float("inf")
#     for a, b in result:
#         if remain <= b:
#             min_value = min(min_value, a)
#         else:
#             another_base = remain // b
#             value = another_base // a
#             min_value = min(min_value, value)
#     print(answer + min_value)

# 100 // 12 = 8, 4
# 당연히 8만큼 7을 곱해야한다고 생각함 -> 56
# 이제 남은 4를 처리해야하므로, 그나마 비용이 적은 7을 선택함 -> 8 * 7 + 7 =63 (오답)
# 100 을 가장 큰 수로 나눠야 한다는 생각부터 틀렸다.
# 더 작은 수로 나눈 후, 다른 수의 합으로 그 공백을 메울 수 있다.
# 7 * 6 = 42원 -> 12 * 6 = 72명 -> 28명 남은. 20원만 넣으면 30명 채우기 가능
# 반면 28명을 채우기 위해, 12 * 3 -> 7 * 3: 21원 필요함.
# 그렇다면... 하나씩 채워나가야하나 -> 서서히 올린다 : 몇명이 남는지 본다 -> 남은 수를 최소 비용으로 채울 숫자가 등장 -> 그걸로 대체.
answer = 0
i = 1

while True:
    remain = C - (result[0][1] * i)
    answer = result[0][0] * i
    # 얘를 채울 다른 수가 있는지 판단. 없으면 continue
    for a, b in result[1:]:
        if remain <= b:
            answer += a  # 찾음 # a 를 더하면 끝
            print(answer)
            exit(0)
            break
    else:
        i += 1
        continue
# remain 이 2일 때, 1은 아예 걸러버리네. 그래서 오답뜸.
# 1을 걸러 버릴게 아니라. 2를 충족시킬 때 가장 비용이 적게 드는 걸 골라야 함.
# (1,1) -> 2, (3, 5) -> 3 : 결국 답은 (1,1)
# result 길이는 20 이하.

"""
대충 노력하고, 엄청 열심히 산 것으로 착각하지 말자. 

9원 들여 홍보 -> 3명 고객 늘어남
9원의 정수배 만큼 투자하면 그 배수 만큼 고객 늘어남. 

C 명을 늘리기 위해 투자해야하는 돈의 최솟값. 

도시 개수 N

3원 5명
1원 1명

12명을 넘겨야함. 
이 때 드는 최소 비용
6원이면 10명
2원이면 2명

비율을 구하자. 투자대비 이율 -> b/a 이게 비율, 이게 큰대로 정렬

------
10명

1/3 = 0.33
2/2 = 1
3/1 = 3

3원 -> 9명

1명만 더 채우면 된다. 
3원 1명
2원 2명
1원 3명 -> 언뜻 보기엔 3원을 해야할 것 같지만, 걍 1원 하는게 맞다.

10 10
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10

이율이 모두 같다. 
그럴 땐, 넘겨야 하는 수를 가장 빠르게 맞출 수 있는 (큰) 수를 고르는게 맞다. 

돈 / 명

100 6
2.25 -> 44원 : 99명 + 1원 : 2명 => 100보다 같거나 커짐.
1.11
1.11
0.9
2
0.99

C // [1] -> * [0] => C - temp = remains
"""
