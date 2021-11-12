# 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def bfs(n, start, graph):
    q = deque([start])
    dist = [0] * (n + 1)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dist[i] == 0 and i != start:
                dist[i] = dist[now] + 1
                q.append(i)
    return dist.count(max(dist))

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    return bfs(n, 1, graph)