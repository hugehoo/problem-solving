N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_dp = [[0] * N for _ in range(N)]
max_dp = [[0] * N for _ in range(N)]
min_ = board[0][0]
max_ = board[N - 1][N - 1]



for d in dp:
    print(d)

"""
모든 경로 -> 최소, 최대 => dp배열을 2개로 두면 안되나. 아니면 하나의 배열에 원소를 (r,c) 묶어서 2개 넣던지
숫자가 작아서 모든 경로를 다 저장해도 될 것 같은데.
"""
