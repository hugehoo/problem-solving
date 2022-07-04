import sys
from itertools import permutations

input = sys.stdin.readline

word = list(input().rstrip())
word_dict = {}
for w in word:
    word_dict[w] = word_dict.get(w, 0) + 1

not_palindrome = 0
for n in word_dict.values():
    if n % 2 != 0:
        not_palindrome += 1
    if not_palindrome > 1:
        print("I'm Sorry Hansoo")
        exit()

odd = []
even = []
center = ''
part_set = []

for k, v, in word_dict.items():
    if v % 2 != 0:
        odd += ([k] * ((v - 1) // 2))
        center = k
    else:
        even += ([k] * (v // 2))
total = even + odd
total.sort()
part_set = ''.join(total)
front = part_set
back = front[::-1]
print(front + ''.join(center) + back)

"""
딕셔너리로 알파벳별 갯수 구한다.
알파벳 갯수가 홀수 일 때,  
"""
