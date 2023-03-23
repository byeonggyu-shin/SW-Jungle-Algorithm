#  Dijkstra - 최단경로

# import sys

# v, e = map(int, sys.stdin.readline().split())
# k = int(sys.stdin.readline())

# graph = [[] for _ in range(e + 1)]
# visited = [False] * (v + 1)
# distance = [float('inf')] * (e + 1)

# for _ in range(e):
#     u, v, w=  map(int, sys.stdin.readline().split())
#     graph[u].append((v, w))

# def get_smallest_node():
#     min_value = float('inf')
#     index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
#     for i in range(1, e + 1):
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
#     for i in range(v - 1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
#         now = get_smallest_node()
#         visited[now] = True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# # 다익스트라 알고리즘을 수행
# dijkstra(k)
# # 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1, v + 1):
#     # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
#     if distance[i] == float('inf'):
#         print("INF")
#     # 도달할 수 있는 경우 거리를 출력
#     else:
#         print(distance[i])


import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(v + 1)]
distance = [float('inf')] * (v + 1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, v + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == float('inf'):
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
