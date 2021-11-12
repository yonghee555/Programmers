# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def bfs(start, n, computers, visited):
    visited[start] = True
    q = deque([start])
    while q:
        now = q.popleft()
        for i in range(n):
            if now == i: continue
            if computers[now][i] and not visited[i]:
                visited[i] = True
                q.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, n, computers, visited)
            answer += 1
    return answer