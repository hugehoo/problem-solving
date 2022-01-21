import heapq


result = []
while True:
    try:
        arr = list(map(str, input().split()))
        result += arr
        if arr == -1:
            break
    except EOFError:
        break

N = result[0]
heap = []
for i in result[1:]:
    print(int(i[::-1]))
    heapq.heappush(heap, int(i[::-1]))
while heap:
    answer = heapq.heappop(heap)
    print(answer)


li = list()
cnt = 0
while 1:
    try:
        ins = input()
        if ins == -1:
            break
        else:
            i_sp = ins.split()
            for i in i_sp:
                if cnt != 0:
                    i = "".join(reversed(i)).lstrip("0")
                    li.append(int(i))
                cnt += 1
    except EOFError:
        break

res = sorted(li)
for i in res:
    print(i)
