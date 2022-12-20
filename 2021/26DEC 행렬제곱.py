import sys


def matrix_mul(A, B):
    temp = [[0] * len(A) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k]
                temp[i][k] = temp[i][k] % 1000
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n // 2)
        return matrix_mul(temp, temp)
    else:
        temp = matrix_pow(A, n - 1)
        return matrix_mul(temp, A)


read = sys.stdin.readline
N, M = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(N)]
print(matrix_pow(matrix, M))

"""
2 5
1 2
3 4
"""
