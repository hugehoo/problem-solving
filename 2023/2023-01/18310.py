N = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[(N - 1) // 2])

"""
4
5 1 7 9
-> 4 + 0 + 2 + 4 = 8
-> 5 + 1 + 1 + 3 = 10

3
1 7 9 
-> 6 + 0 + 2 = 8
-> 4 + 2 + 4 = 8

5
1 2 6 8 10
-> 5 + 2 + 0 + 2 + 4 = 13
-> 4 + 3 + 1 + 3 + 5 = 16



"""
