from collections import Counter
def solution(tasks):
    answer = 0
    task_count = Counter(tasks)
    for k, v in task_count.items():
        if v == 1:
            return -1
        # if v == 2 or v == 3:
        #     continue
        # else:
        #     task_count[k] = v - 3
        if find_smallest_number_not_sum_of_2_and_3(v):
            return -1
    return answer
"""
2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
"""

print(solution([1, 1, 2, 2]))
print(solution([4, 1, 1, 1, 1, 2, 3]))
def find_smallest_number_not_sum_of_2_and_3():
    nums = set()
    for i in range(100):  # 임의로 100 이하의 수를 선택
        for j in range(100):
            num = 2*i + 3*j
            if num <= 100:
                nums.add(num)
    for i in range(2, 100):
        if i not in nums:
            return i
print(find_smallest_number_not_sum_of_2_and_3())