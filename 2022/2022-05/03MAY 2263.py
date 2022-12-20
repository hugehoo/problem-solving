import sys

input = sys.stdin.readline

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (n + 1)
for i in range(n):
    position[inorder[i]] = i


def divide(in_start, in_end, p_start, p_end):
    if (in_start > in_end) or (p_start > p_end):
        return
    # 후위 순회로 부터 부모 찾기
    parents = postorder[p_end]
    print(parents, end=" ")

    # left 인자 개수
    left = position[parents] - in_start

    # right 인자 개수
    right = in_end - position[parents]

    # 왼쪽 노드
    divide(in_start, in_start + left - 1, p_start, p_start + left - 1)

    # 오른쪽 노드
    divide(in_end - right + 1, in_end, p_end - right, p_end - 1)

divide(0, n - 1, 0, n - 1)

"""
preorder : 루트 - 왼쪽 - 오른쪽 <- 구하고자 하는 것. 
inorder : 왼쪽 - 루트 - 오른쪽
postorder : 왼쪽 - 오른쪽 - 루트

n = 1 
왼쪽(=루트)

n = 2 
왼쪽과 루트

n = 4
첫번째가 왼쪽인건 확실..?

"""
