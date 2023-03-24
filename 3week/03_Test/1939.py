#  중량제한
# 예제 케이스만 통과함

import sys
from collections import deque

def bfs(start,end):
    visited = [False] * (n + 1)

    # 더 작은 값을 찾아야하니 초기값 무한
    q = deque([(start, float('inf'))]) 
    
    while q:
        cur, cur_weight = q.popleft()
        # 도착하면 끝
        if cur == end:
            return cur_weight
        
        if visited[cur]:
            continue

        for next, w in roads[cur]:
            if not visited[next]:
                q.append((next, min(cur_weight, w))) 
    return -1
        
n, m = map(int, sys.stdin.readline().split())

roads = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    roads[u].append((v ,w) )
    roads[v].append((u ,w) )

a,b = map(int, sys.stdin.readline().split())

print(bfs(a,b))
# print(bfs(1,3))



