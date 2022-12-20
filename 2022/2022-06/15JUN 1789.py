import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    i = 1
    count = 0
    for i in range(2, N):
        for j in range(i, N):
            if N >= j:
                print("- N : ", N, " j : ", j)
                N -= j
                count += 1

            else:
                print("N : ", N, " j : ", j)
                break
        print(count, j)


"""
200 을 만들 수 있는, 서로 다른 자연수 최대의 갯수 : 19개
200 - 1
199 - 2



"""
