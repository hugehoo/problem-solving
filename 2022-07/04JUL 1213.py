import sys
from collections import deque
input = sys.stdin.readline

word = list(input().rstrip())
word_dict = {}
for w in word:
    word_dict[w] = word_dict.get(w, 0) + 1
print(word_dict)

"""
딕셔너리로 알파벳별 갯수 구한다.
알파벳 갯수가 홀수 일 때,  
"""