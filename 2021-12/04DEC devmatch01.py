def solution(drum):
    result = 0
    N = len(drum)

    board = [list(i) for i in drum]

    for c in range(len(board)):
        star_count = 0
        r = 0
        while True:
            point = board[r][c]

            if point == "#":
                r += 1
            elif point == ">":
                c += 1
            elif point == "<":
                c -= 1
            else:
                if star_count < 1:
                    star_count += 1
                    r += 1
                else:
                    break

            if r <= -1 or r >= N or c <= -1 or c >= N:
                break
            if r == (N - 1) and board[r][c] == "#":
                result += 1
                break
            if r == (N - 1) and board[r][c] == "*" and star_count <= 1:
                result += 1
                break
    return result


drum = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]
# drum = ["******", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]
print(solution(drum))
