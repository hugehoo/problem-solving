def solution(N, A, B):
    graph = {i: set() for i in range(1, N + 1)}
    
    assert len(A) == len(B)
    for idx in range(0, len(A)):
        v1 = A[idx]
        v2 = B[idx]
        
        graph[v1].add(v2)
        graph[v2].add(v1)
    for n in range(1, N + 1):
        if n + 1 not in graph[n]:
            return False
    else:
        return True


print(solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]))
print(solution(6, [2, 4, 5, 3], [3, 5, 6, 4]))
print(solution(3, [1, 3], [2, 2]))
