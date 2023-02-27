N = int(input())
T = int(input())
nums = list(map(int, input().split()))
album = {}
for i in range(T):
    if nums[i] in album:
        album[nums[i]][0] += 1
    else:
        if len(album) < N:
            album[nums[i]] = [1, i]
        else:
            temp = sorted(album.items(), key=lambda x: (x[1][0], x[1][1]))
            del album[temp[0][0]]
            album[nums[i]] = [1, i]
album = sorted(album.keys())
print(*album)
