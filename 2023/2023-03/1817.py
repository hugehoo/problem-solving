N, M = map(int, input().split())
count = 0
if N:
    books, bag = list(map(int, input().split())), []
    count = 1
    while books:
        top = books.pop()
        bag.append(top)
        if sum(bag) > M:
            bag = [top]
            count += 1
print(count)

"""
6 10
5 5 5 5 5 5



"""
