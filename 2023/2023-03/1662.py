string = list(input())
input_stack = []
output_stack = []
for s in string:
    if s == ")":
        iter_num = -1
        while 1:
            input_top = input_stack.pop()
            if input_top != "(":
                output_stack.append(input_top)
            else:
                iter_num = input_stack.pop()
                break
        input_stack.append(int(iter_num) * (''.join(output_stack)))
        output_stack = []
    else:
        input_stack.append(s)

answer = ''.join(input_stack)
print(len(answer))