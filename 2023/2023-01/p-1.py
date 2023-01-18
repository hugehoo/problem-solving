import math
import os
import random
import re
import sys


def isPower(arr):
    # Write your code here
    N = 2
    result = []
    for a in arr:
        if a == 0 or a == 1:
            result.append(a)
            continue
        while True:
            b, r = divmod(a, N)
            if b == 1 and r == 0:
                result.append(1)
                break
            elif r == 0:
                a = b
                continue
            else:
                result.append(0)
                break
    return result


# print(isPower([2, 3, 4]))
print(isPower([
    16,
    24,
    56,
    48,
    0,
    1,
    100,
    99,
]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr_count = int(input().strip())
#
#     arr = []
#
#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)
#
#     result = isPower(arr)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
