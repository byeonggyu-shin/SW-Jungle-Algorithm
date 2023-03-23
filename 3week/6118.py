#  Dijkstra - 숨바꼭질

import sys
from collections import deque


def bfs(start):
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1

    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = visited[current_node] + 1
                q.append(next_node)
    return visited


n,m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = bfs(1)
max_distance = max(visited)

barn = visited.index(max_distance)
num_barns = visited.count(max_distance)

print(barn, max_distance - 1, num_barns)