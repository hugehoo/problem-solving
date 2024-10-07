def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
            print(enable_print)
        elif enable_print == 1:
            print(N % 10, end="")
        else:
            print(N % 10, end="")
        N = N // 10


solution(12)
solution(13)
solution(31)
solution(142)
solution(1)
solution(54321)
solution(12345)
solution(100)
solution(1_000_000_000)
"""
10 으로 나눈 나머지.
나머지가 0 이면 ->
"""
