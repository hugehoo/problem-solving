import sys

input = sys.stdin.readline

n = int(input())
# arr = [[1] * 10]
# arr.append([i for i in range(1, 11)])
if n == 1:
    print(10)
    exit()
if n == 2:
    print(55)
    exit()

k = 2
before = [i for i in range(1, 11)]
while k < n:
    # memory over
    # temp = [1]
    # for i in range(1, 10):
    #     temp.append(arr[k - 1][i] + temp[-1])
    # arr.append(temp)
    # k += 1

    # not memo
    temp = [1]
    for i in range(1, 10):
        temp.append(before[i] + temp[-1])
    before = temp
    k += 1
print(sum(before) % 10007)

"""
0이 1개
1이 2개
...
9가 10개
"""
