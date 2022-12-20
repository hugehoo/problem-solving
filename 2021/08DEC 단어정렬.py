N = int(input())
words = list(set(input() for _ in range(N)))

words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)


"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""