import sys

input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
if cranes[0] < boxes[0]:
    print(-1)
    exit()
count = 0
while boxes:
    for c in cranes:
        for b in boxes:
            if c >= b:
                boxes.remove(b)
                break
    count += 1
print(count)
"""
반례

3
20 19 19
5
20 20 19 19 20

3
20 19 19
5
20 20 19 19 19

3
20 10 9
6
17 16 20 15 19 18

while box:
    for c in crane:
        for b in box:
            if c >= b:
                b 첫번째 것 탈락. 덱으로 만들어야할까. 
                break
            else:
                바깥 포문도 끝내고 다시 돌려야함. 왜냐하면 현재의 c 가 그나마 젤 큰데, 현재의 b 도 그나마 젤 큰상황
                그런 상황에서 b 를 못끝낸다? 지금의 c 로써는 운반 불가. 즉 이전의 c 를 가져와야 한다.
                outer_flag = False
        if not outer_flag:
            break
        

"""
