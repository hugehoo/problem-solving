N = int(input())
Apple = int(input())
apples = []
for _ in range(Apple):
    apples.append(map(int, input().split()))

D = int(input())
directions = []
times = []
for _ in range(D):
    t, d = map(str, input().split())
    times.append(int(t))
    if d == "D":
        directions.append([1, 0])
    if d == "L":
        directions.append([0, -1])
    if d == "R":
        directions.append([0, 1])
    if d == "U":
        directions.append([-1, 0])

board = [[0] * N for _ in range(N)]
for r, c in apples:
    board[r - 1][c - 1] = "X"
for b in board:
    print(b)

start = [0, 0]
R = [0, 1]
D = [1, 0]
L = [0, -1]
U = [-1, 0]

curr_dir = R
time = 0
tail = start
while True:
    curr_r, curr_c = start
    plus_r, plus_c = curr_dir
    start = [curr_r + plus_r, curr_c + plus_c]
    time += 1
    if 0 > start[0] or start[0] >= N or 0 > start[1] or start[1] >= N:
        break
    if board[start[0]][start[1]] != 0 and board[start[0]][start[1]] != "X":
        break
    if board[start[0]][start[1]] == "X":
        board[start[0]][start[1]] = time
    else:
        board[tail[0]][tail[1]] = 0
        # tail = [curr_r, curr_c]
        board[start[0]][start[1]] = time

    if time in times:
        idx = times.index(time)
        curr_dir = directions[idx]

print(time)
"""
부분합이 m이 되도록

1) e == N 이면 s++
2) s == e 이면 e ++
3) sum = M 이면 e ++
4) sum < M 이면 e ++ 
5) M < sum 이면 s ++  
"""

class Empty(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def _resize(self, n):
        old = self._data
        self._data = [None] * n
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer