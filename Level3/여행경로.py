# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

def dfs(departure, path, tickets, count, used, n):
    if n == count:
        global answer
        path.append(departure)
        answer.append(path)
        return
    for i in range(n):
        if not used[i] and tickets[i][0] == departure:
            used[i] = True
            new_path = path + [tickets[i][0]]
            dfs(tickets[i][1], new_path, tickets, count + 1, used, n)
            used[i] = False

def solution(tickets):
    global answer
    answer = []
    n = len(tickets)
    used = [False] * n
    dfs("ICN", [], tickets, 0, used, n)
    answer.sort()
    return answer[0]