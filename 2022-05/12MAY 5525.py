import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
string = list(input().strip())
print(string)
i = 0
partial = ""

O = ['O'] * n
I = ['I'] * n
Pn = ""
for _ in range(n):
    Pn += "I"
    Pn += "O"
Pn += "I"

print(Pn)
count = 0


def check_partial(partials: str):
    global i
    global string
    global partial
    if partials and partials[0] == "O":
        string = string[i + 1:]
        partial = ''
        i = 0
        return False

    return partials == Pn


while i < len(string) - 1:
    if check_partial(partial):
        count += 1
        partial = ''
        string = string[i + 1:]
        i = 0
        continue

    if string[i] == string[i + 1]:
        string = string[i + 1:]
        partial = ''
        i = 0
        continue
    else:
        partial += string[i]
        i += 1
        continue
print(count)