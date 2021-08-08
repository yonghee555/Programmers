# 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def solution(N, road, K):
    answer = 0
    graph = {}
    for i in range(N + 1):
        graph[i] = {}

    for t1, t2, dist in road:
        if t2 not in graph[t1]:
            graph[t1][t2] = dist
        else:
            graph[t1][t2] = min(dist, graph[t1][t2])
        if t1 not in graph[t2]:
            graph[t2][t1] = dist
        else:
            graph[t2][t1] = min(dist, graph[t2][t1])
    distances = dijkstra(graph, 1)
    for dist in distances.values():
        if dist <= K:
            answer += 1

    return answer

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue
        for next_node, new_distance in graph[node].items():
            distance = current_distance + new_distance
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances