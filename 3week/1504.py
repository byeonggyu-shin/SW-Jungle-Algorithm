#  Dijkstra - 특별한 최단경로

# import sys
# n,e = map(int, sys.stdin.readline().split())

# graph = [[] for _ in range(n+1)]
# distance = [float('inf')] * (n + 1)

# for _ in range(e):
#     a,b,c = map(int, sys.stdin.readline().split())
#     graph[a].append((b, c))

# u,v = map(int, sys.stdin.readline().split())

# arv = [1,u,v,n]

# def get_smallest_node():
#     min_value = float('inf')
#     index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
#     for i in range(1, n + 1) :
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
#     for i in range(n - 1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now = get_smallest_node()
#         visited[now] = True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost


# answer = 0
# for i in range(len(arv)-1):
#     visited = [False] * (n + 1)
#     dijkstra(i)
#     answer += distance[i+1]
#     distance = [float('inf')] * (n + 1)
#  => 3번 진행하고 3번 모두 모든 노드의 최소를 구해야함 
# print(answer)


import heapq
import sys

input = sys.stdin.readline

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n + 1)
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 양방향 그래프
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 1 -> v1 -> v2 -> N 순서로 방문
d1 = dijkstra(1, graph, n)
d_v1 = dijkstra(v1, graph, n)
d_v2 = dijkstra(v2, graph, n)

result1 = d1[v1] + d_v1[v2] + d_v2[n]

# 1 -> v2 -> v1 -> N 순서로 방문
result2 = d1[v2] + d_v2[v1] + d_v1[n]

result = min(result1, result2)

if result == float('inf'):
    print(-1)
else:
    print(result)
