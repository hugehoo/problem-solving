N = int(input())
M = int(input())

result = [list(map(int, input().split())) for _ in range(M)]

friend = set()
for a, b in result:
    if a == 1 or b == 1:
        friend.add(b)
        friend.add(a)

friend_friend = set()
for a, b in result:
    if a in friend or b in friend:
        friend_friend.add(a)
        friend_friend.add(b)

friend_friend = friend_friend.difference(friend)
try:
    friend.remove(1)
except KeyError:
    pass

print(len(friend)+len(friend_friend))
