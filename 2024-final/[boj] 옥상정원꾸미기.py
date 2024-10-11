from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input())
    buildings = [int(input()) for _ in range(N)]
    stack = [buildings[0]]
    result = 0
    for i in range(1, N):
        while stack and stack[-1] <= buildings[i]:
            stack.pop()
        stack.append(buildings[i])
        result += (len(stack) - 1)
    print(result)
