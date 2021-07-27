def solution(dirs):
    answer = 0
    command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    path = []
    x = 0
    y = 0
    for c in dirs:
        a = command[c][0]
        b = command[c][1]
        if a != 0 and abs(x + a) <= 5:
            if (x, x + a, y, y) not in path:
                path.append((x, x + a, y, y))
                path.append((x + a, x, y, y))
                answer += 1
            x += a
        if b != 0 and abs(y + b) <= 5:
            if (x, x, y, y + b) not in path:
                path.append((x, x, y, y + b))
                path.append((x, x, y + b, y))
                answer += 1
            y += b
    return answer