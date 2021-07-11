def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])
    while True:
        erase_set = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != '0':
                    erase_set.add((i, j))
                    erase_set.add((i + 1, j))
                    erase_set.add((i, j + 1))
                    erase_set.add((i + 1, j + 1))
        temp = answer
        for i, j in erase_set:
            board[i][j] = '0'
            answer += 1

        if temp == answer:
            break
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if board[i][j] != '0':
                    continue
                x = i
                while x >= 0 and board[x][j] == '0':
                    x -= 1
                if x >= 0:
                    board[i][j] = board[x][j]
                    board[x][j] = '0'

    return answer
