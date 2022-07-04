import sys
from collections import Counter

input = sys.stdin.readline

word = input().rstrip()
word_dict = Counter(word)
odd, even, center = [], [], ''

if len(list(filter(lambda x: x % 2 != 0, word_dict.values()))) > 1:
    print("I'm Sorry Hansoo")
    exit()

for k, v, in word_dict.items():
    if v % 2 != 0:
        odd = ([k] * ((v - 1) // 2))
        center = k
    else:
        even += ([k] * (v // 2))

total = sorted(even + odd)
front = ''.join(total)

print(front + center + front[::-1])

"""
딕셔너리로 알파벳별 갯수 구한다.
알파벳 갯수가 홀수 일 때,  
"""
