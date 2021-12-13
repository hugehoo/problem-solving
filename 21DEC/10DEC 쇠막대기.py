N = list(map(str, list(input())))
stack = []
layer = dict()
cur_layer = 0
count = 0


def handle_layer():
    for k, v, in layer.items():
        layer[k] += 1


for idx, n, in enumerate(N):
    if n == "(":
        try:
            if stack[-1] == "(":
                cur_layer += 1
                layer[cur_layer] = 0
                stack.append(n)
        except:
            pass
    else:
        if stack[-1] == "(":
            for k, v in layer:
                layer[k] += 1
            stack.pop()
print(layer)


    # if idx < len(N) - 1:
    #     if n == "(":
    #         if N[idx + 1] == '(':
    #             cur_layer += 1
    #             layer[cur_layer] = 1
            # else:
            #     print('--')
            #     handle_layer()
        # else:
        #     count += layer[cur_layer]
        #     cur_layer -= 1
print(layer)
print(count)
"""
()(((()())(())()))(())
"""
