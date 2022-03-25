def solution(n, k, cmd):
    cur = k
    table = {
        i: [i - 1, i + 1] for i in range(n)
    }
    answer = ['O'] * n
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []

    for c in cmd:
        if c == "C":
            answer[cur] = "X"
            prev, next_ = table[cur]
            stack.append([prev, cur, next_])

            if not next_:  # if not next_ 와 if next_ == None 은 다른 결과를 출력
                cur = table[cur][0] #prev  # table[cur][0]
            else:
                cur = table[cur][1] # next_  # table[cur][1]

            if not prev:
                table[next_][0] = None
            elif not next_:
                table[prev][1] = None
            else:
                table[prev][1] = next_
                table[next_][0] = prev

        elif c == "Z":
            prev, now, next_ = stack.pop()
            answer[now] = "O"
            if not prev:
                table[next_][0] = now
            elif not next_:
                table[prev][1] = now
            else:
                table[next_][0] = now
                table[prev][1] = now
        else:
            # 커서 이동
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]
            # direction, count = c.split(" ")
            # for _ in range(int(count)):
            #     if direction == "D":
            #         cur = table[cur][1]
            #     else:
            #         cur = table[cur][0]
    return "".join(answer)


# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
# print(solution(5, 0, ["C", "D 3", "C", "C"]))
ta = {
    "0" : None
}
print(ta["0"], not ta["0"])