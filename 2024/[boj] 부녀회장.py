import sys

input = sys.stdin.readline
N = int(input())
while N > 0:
    k = int(input())  # 층
    n = int(input())  # 호
    
    below = [i for i in range(n + 1)]
    # if k == 1:
    #     print(n)
    #     N -= 1
    #     continue
    level = 1
    while k >= level:
        upper = [0] * (n + 1)
        for j in range(1, n + 1):
            upper[j] = below[j] + upper[j - 1]
        below = upper
        level += 1
        print(below[n])
    
    N -= 1
    
    """
    자기 바로 밑의 층 배열을 구해야 한다.
    그러려면 그 밑의 층 배열도 알아야함.

    1 4 10
    1 3 6
    1 2 3
    """
