import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
tree_dict = defaultdict(list)

for _ in range(N):
    node, left, right = input().strip().split(" ")
    if left == ".":
        left = None
    if right == ".":
        right = None

    tree_dict[node] = [left, right]
print(tree_dict)
""" 전위
루트 - left - right
"""
left_queue = deque()
right_queue = deque()
root = deque()
root.append("A")
left, right = tree_dict["A"]

if left:
    left_queue.append(left)
if right:
    right_queue.append(right)
answer = ["A"]
while left_queue or right_queue:
    while left_queue:
        pops = left_queue.popleft()
        answer.append(pops)
        left_, right_ = tree_dict[pops]
        if left_:
            left_queue.append(left_)
        if right_:
            right_queue.append(right_)
    while right_queue:
        pops = right_queue.popleft()
        answer.append(pops)
        left_, right_ = tree_dict[pops]
        if left_:
            left_queue.append(left_)
        if right_:
            right_queue.append(right_)
        if left_queue:
            break
print(answer)
