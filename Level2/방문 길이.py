def solution(dirs):
    answer = 0
    command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    path = []
    x = 0
    y = 0
    for c in dirs:
        if command[c][0] != 0 and abs(x + command[c][0]) <= 5:
            if (x, x + command[c][0], y, y) not in path:
                path.append((x, x + command[c][0], y, y))
                path.append((x + command[c][0], x, y, y))
                answer += 1
            x += command[c][0]
        if command[c][1] != 0 and abs(y + command[c][1]) <= 5:
            if (x, x, y, y + command[c][1]) not in path:
                path.append((x, x, y, y + command[c][1]))
                path.append((x, x, y + command[c][1], y))
                answer += 1
            y += command[c][1]
    return answer