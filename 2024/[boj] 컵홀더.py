import sys

input = sys.stdin.readline
N = int(input())
origin_input = list(map(str, input().strip()))
seats = ['*']
l_seat = []
for seat in origin_input:
    if seat == 'S':
        seats.append(seat)
        seats.append('*')
    if seat == 'L':
        l_seat.append(seat)
        if len(l_seat) == 2:
            l_seat = []
            seats.append(seat)
            seats.append(seat)
            seats.append('*')

idx, holder, person, non_holder = 0, 0, 0, 0
while idx < len(seats):
    if seats[idx] == '*':
        holder += 1
    
    if seats[idx] == 'L' or seats[idx] == 'S':
        if person >= 1:
            person = 0
            non_holder += 1
        person += 1
    
    if holder == 1 and person == 1:
        holder = 0
        person = 0
    
    idx += 1
print(N - non_holder)
"""
index 로 순회
앞뒤 하나라도 별이 있으면 별과 함께 pop
*S *L L* L L* S* S* L L*

"""
