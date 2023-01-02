N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = 0
K = 0
square_area = (K * K + (K + 1) * (K + 1))


def find(r, c):
    global K
    global max_value
    in_square = 0
    if K == 0 and board[r][c]:
        in_square += 1
        max_value = max(max_value, in_square)
        return
    
    for r_ in range(K + 1):
        for k in range(K - r_, -K - 1 + r_, -1):
            if (0 <= c + k < N) and (0 <= r + r_ < N) and board[r + r_][c + k]:
                in_square += 1
            if r_ > 0:
                if (0 <= r + -r_ < N) and (0 <= c + k < N) and board[r + -r_][c + k]:
                    in_square += 1
    
    cost = (in_square * M) - square_area
    if cost >= 0:
        max_value = max(max_value, in_square)


while K <= 20:
    for r in range(N):
        for c in range(N):
            find(r, c)
    K += 1
print(max_value)
"""
최대 금의 개수를 우선 찾고(개수 x 개별 가격), 비용이 그보다 큰 마름모는 계산할 필요도 없다.

(max_value - 마름모의 넓이) 가 가장 큰 케이스

마름모의 넓이를 어떻게 점진적으로 넓히느냐.

5 5
0 0 0 0 0
0 1 0 0 0
0 0 1 0 1
0 0 0 0 0
0 0 0 1 0

5 5
0 0 1 0 0
0 2 2 2 0
1 2 3 2 1
0 2 2 2 0
0 0 1 0 0


4 4
0 0 1 0
0 1 2 1
0 1 1 0
0 0 0 0
"""
