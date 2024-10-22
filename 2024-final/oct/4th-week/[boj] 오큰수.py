from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    nums = list(map(int, input().split()))
    NGE = []
    stack =[]
    for i in range(len(nums) - 1, -1, -1):
        target = nums[i]
        if len(stack) == 0:
            NGE.append(-1)
            stack.append(target)
        else:
            while target >= stack[-1]:
                temp = stack.pop()
                if not stack:
                    stack.append(-1)
                    break
            NGE.append(stack[-1])
            stack.append(target)
    print(*NGE[::-1])
    
    """
    크면서 가장 가까운 수 .
    그냥 큰 수가 아니라 가장 가까운 수
    """

"""
4
3 5 2 7

4
9 5 4 8

5
2 1 2 3 5


뒤에서 부터 탐색
스택이 비어있으면 -1 삽입
스택의 수랑 탐색 대상이랑 비교

탐색 대상이 더 크면 -1
작으면 스택에 탐색 대상 넣음.
"""
