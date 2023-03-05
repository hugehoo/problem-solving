
N, M = map(int, input().split())
if not N:
    print(0)
    exit()
    
nums = list(map(int, input().split()))
bag = []
L = len(nums)
count = 1
while nums:
    top = nums.pop()
    bag.append(top)
    if sum(bag) > M:
        bag = [top]
        count += 1
print(count, bag)



"""
6 10
5 5 5 5 5 5
"""