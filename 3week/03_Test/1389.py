# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

def bfs(start):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    q = deque([start])
    
    
    while q:
        cur = q.popleft()
        visited[cur] = True
        for next in friends[cur]:
            if not visited[next]:
                visited[next] = True
                dist[next] = dist[cur] + 1
                q.append(next)

    return dist
        
n, m = map(int, sys.stdin.readline().split())

friends = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

distance = [float('inf')] * (n + 1)
result = [[] for _ in range(n+1)]

result = float('inf')
answer = 0
for i in range(1,n+1):
    if sum(bfs(i)) < result:
        result = sum(bfs(i))
        answer = i

print(answer)

