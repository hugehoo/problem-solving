K = int(input())
for k in range(K):
    print("Class %d" %(k + 1))
    arr = list(map(int, input().split()))
    num, numbers = arr[0], sorted(arr[1:], reverse=True)
    max_v = 0
    for i in range(len(numbers) - 1):
        if max_v < numbers[i] - numbers[i + 1]:
            max_v = numbers[i] - numbers[i + 1]
    print("Max %d, Min %d, Largest gap %d" % (max(numbers), min(numbers), max_v))
