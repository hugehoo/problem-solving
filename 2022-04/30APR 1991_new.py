import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
tree_dict = {}

for _ in range(N):
    node, left, right = input().strip().split(" ")
    tree_dict[node] = [left, right]


def preorder(root):
    if root != ".":
        print(root, end='')
        preorder(tree_dict[root][0])
        preorder(tree_dict[root][1])


def inorder(root):
    if root != ".":
        inorder(tree_dict[root][0])
        print(root, end="")
        inorder(tree_dict[root][1])


def postorder(root):
    if root != ".":
        postorder(tree_dict[root][0])
        postorder(tree_dict[root][1])
        print(root, end="")


preorder("A")
print('')
inorder("A")
print('')
postorder("A")
