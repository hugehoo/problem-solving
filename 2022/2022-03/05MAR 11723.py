import sys

n = int(sys.stdin.readline())
result = set()
for _ in range(n):
    # arr = list(map(str, sys.stdin.readline().split())) # map() 을 사용하면 시간 초과가 발생한다. 왜..?
    arr = map(str, sys.stdin.readline().split())
    print(arr)

    if len(arr) == 1:
        cmd = arr[0]
        if cmd == "all":
            result = set([i for i in range(1, 21)])
        else:
            result = set()
    else:
        cmd = arr[0]
        value = int(arr[1])

        if cmd == "add":
            result.add(value)
        elif cmd == "check":
            print(1 if value in result else 0)
        elif cmd == "remove":
            result.discard(value)
        elif cmd == "toggle":
            if value in result:
                result.discard(value)
            else:
                result.add(value)
