def solution(n, k, cmd):
    origin = []
    for i in range(n):
        origin.append(i)

    curr_idx = k
    remove_stack = []
    for c in cmd:
        if c == "C":
            remove_stack.append([curr_idx, origin[curr_idx]])
            if curr_idx == len(origin) - 1:
                del origin[curr_idx]
                curr_idx = len(origin) - 1
            else:
                del origin[curr_idx]
            # 끝단을 지울 때 curr_idx 를 세팅해줘야한다.
            # 첫단을 지울 땐 그대로 0으로 돼있다.
            # 끝단을 지우면 origin 의 len() 보다 -1 인 값을 세팅한다.

        elif c == "Z":  # 복구시 curr_idx 는 변하지 않는다. 문제는 curr_idx 보다 이전 것이 복구되면, 자연히 curr_idx 는 1씩 증가해야한다.
            pops = remove_stack.pop()
            if pops[0] <= curr_idx:
                curr_idx += 1
                origin.insert(pops[0], pops[1])
            else:
                origin.insert(pops[0], pops[1])
        else:
            direction, count = c.split(" ")
            if direction == "D":
                curr_idx += int(count)
            else:
                curr_idx -= int(count)
    result = []
    for i in range(n):
        result.append(i)
    answer = ""
    for i in result:
        if i in origin:
            answer += "O"
        else:
            answer += "X"
    # print(curr_idx)
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
print(solution(5, 0, ["C", "D 3", "C", "C"]))
