# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(a: list[int]):
    # Implement your solution here
    num_array = sorted(a)
    for i in range(len(num_array) - 1):
        if abs(num_array[i] - num_array[i + 1]) == 1:
            return True
    else:
        return False

#
print(solution([7]))
print(solution([4, 3]))
print(solution([11, 1, 8, 12, 14]))
print(solution([5, 5, 5, 5, 5]))

import random

my_list = [random.randint(1, 1000000000) for _ in range(1000000)]

print(solution(my_list))
"""
1_000_000_000
"""

"""sql
SELECT place
FROM table_name
GROUP BY place
HAVING SUM(CASE WHEN opinion = 'recommended' THEN 1 ELSE 0 END) >
       SUM(CASE WHEN opinion = 'not recommended' THEN 1 ELSE 0 END)
ORDER BY place ASC
"""