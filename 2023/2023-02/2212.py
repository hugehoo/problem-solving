sensor = int(input())
center = int(input())
sensor_list = sorted(list(map(int, input().split())))
if sensor <= center:
    print(0)
    exit(0)
distance = sorted([(sensor_list[i] - sensor_list[i - 1]) for i in range(1, len(sensor_list))], reverse=True)
for c in range(center - 1): distance[c] = 0
print(sum(distance))

"""
구해야 하는 것 : center 수 만큼의 구간이 최소 길이가 되는 값
우리는 각 구간이 얼마인지 알 필요 없다.
그저 구간을 모두 더했을 때 최소 값이 나오면 된다.
그러기 위해 우선 구간을 추린 후 내림차순 정렬한다.
정렬된 구간에서 가장 큰 구간부터 (센터 수보다 하나 적게) 차례대로 제거한다.
왜 센터 수보다 하나 작게인가?
센터의 수만큼 구간이 생기기 때문이다.
센터가 하나라고 해보자.
구간은 하나가 생긴다.
센터가 둘이라고 해보자.
구간은 두개가 생긴다.
구간을 하나 없앤다는 건, 두개의 뭉텅구간이 생긴 다는 것.
"""

# n = int(input())
# k = int(input())
# data = list(map(int,input().split()))
# lst = []
# data.sort()
#
# for i in range(1,n):
#     lst.append(data[i]-data[i-1])
#
# lst.sort(reverse=True)
# print(lst)
# for i in range(k-1):
#     lst[i]=0
# print(lst)
#
# result = sum(lst)
#
# print(result)
"""
6
2
1 6 9 3 6 7

6
2
1 3 7 7 8 10
"""
