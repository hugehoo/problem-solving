from math import factorial

for idx, i in enumerate(reversed(str(factorial(int(input()))))):
    if i != '0':
        print(idx)
        break
