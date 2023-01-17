N = int(input())

arr = list(map(str, input().strip()))
count_r, count_b = 0, 0

for idx, value, in enumerate(arr):
    if idx + 1 == len(arr) or value != arr[idx + 1]:
        if value == "B":
            count_b += 1
        else:
            count_r += 1
print(min(count_b, count_r) + 1)

"""
mincount 가 연속됐을 때. 

민카운트가 문제가 아닐지도.
서로 연결된 색이 몇개이느냐. 
연속된 것들이 얼마나 있느냐, 

연속된 것들은 결국 하나. 몇개가 연속되는 결국 하나로 볼 수 있다. 
그 연속된 것들을 하나로 치환하고, 각 색깔의 민카운트 구한다. 그후 + 1

B
B
B
B
R
B
R
B
R

8
BBRBRBBR

11
BBBRRRBBRRB
"""
