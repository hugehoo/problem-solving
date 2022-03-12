from collections import deque


def solution(n, clockwise):
    board = [[0] * n for _ in range(n)]
    start_point = [[0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]]
    sequence = deque()
    first = (0, '+')
    second = ("+", 0)
    third = ("0", "-")
    fourth = ("-", 0)
    # for i in [first, second, third, fourth]:
    #     sequence.append(i)

    while True:

        for idx, ele in enumerate(start_point):

            row = ele[0]
            col = ele[1]
            num = 1
            pad = 1
            if idx == 0:
                for i in [first, second, third, fourth]:
                    sequence.append(i)
            elif idx == 1:
                for i in [second, third, fourth, first]:
                    sequence.append(i)
            elif idx == 2:
                for i in [third, fourth, first, second]:
                    sequence.append(i)
            elif idx == 3:
                for i in [fourth, first, second, third]:
                    sequence.append(i)

            flag = True
            print(idx)
            while sequence:
                direction = sequence.popleft()
                if direction == first:
                    for i in range(n - pad):
                        if board[row][col] != 0:
                            flag = False
                        board[row][col] = num
                        if i != (n - pad - 1):
                            col += 1
                        num += 1
                if direction == second:
                    for _ in range(n - pad):
                        row = row + 1
                        if board[row][col] != 0:
                            flag = False
                        board[row][col] = num
                        num += 1
                if direction == third:
                    for _ in range(n - pad):
                        col -= 1
                        if board[row][col] != 0:
                            flag = False
                        board[row][col] = num
                        num += 1
                if direction == fourth:
                    for _ in range(n - pad):
                        row -= 1
                        if board[row][col] != 0:
                            flag = False
                        board[row][col] = num
                        num += 1
                        sequence.append(first)
                pad += 1
                # print('flag ', flag)
                if not flag:
                    break
        break
    for b in board:
        print(b)
    answer = [[]]
    return answer


solution(5, True)
# solution(6, False)
