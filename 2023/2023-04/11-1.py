# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(n: int):
    n_list = list(str(n))
    n_list.sort(reverse=True)
    return int(''.join(n_list)) if int(''.join(n_list)) <= 100_000_000 else -1


print(solution(213))
print(solution(553))
print(solution(2_147_483_647))
