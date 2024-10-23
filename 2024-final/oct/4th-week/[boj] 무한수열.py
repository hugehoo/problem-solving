from sys import stdin

input = stdin.readline


def recursive(param: int) -> int:
    if A.get(param):
        return A[param]
    A[param] = recursive(param // P) + recursive(param // Q)
    return A[param]


if __name__ == '__main__':
    N, P, Q = map(int, input().split())
    A = {0: 1}
    
    print(recursive(N))
    print(A)
