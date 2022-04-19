def solution(n, k, cmd):
    origin = []
    for i in range(n):
        origin.append(i)

    curr_idx = k
    remove_stack = []
    for c in cmd:
        if c == "C":
            remove_stack.append([curr_idx, origin[curr_idx]])
            del origin[curr_idx]
        elif c == "Z":
            pops = remove_stack.pop()
            origin.insert(pops[0], pops[1])
        else:
            direction, count = c.split(" ")
            if direction == "D":
                curr_idx += int(count)
            else:
                curr_idx -= int(count)
    result=[]
    for i in range(n):
        result.append(i)
    answer = ""
    for i in result:
        if i in origin:
            answer += "O"
        else:
            answer += "X"
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
