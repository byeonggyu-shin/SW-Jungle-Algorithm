#  완전탐색
import sys
from itertools import permutations

n = int(sys.stdin.readline())
dist = []
for _ in range(n):
    dist.append(list(map(int, sys.stdin.readline().split())))

cities = [i for i in range(n)]
perm = permutations(cities, n)

min_cost = float('inf')

for p in perm:
    start = p[0]
    cost = 0
    path = True
    for i in range(1, n):
        if dist[p[i-1]][p[i]] == 0:
            path = False
            break
        else:
            cost += dist[p[i-1]][p[i]]
            if cost > min_cost:
                break
              
    if path and dist[p[-1]][start] != 0:
        cost += dist[p[-1]][start]
        if cost < min_cost:
            min_cost = cost

print(min_cost)

#  동적 프로그래밍을 활용한 TSP 알고리즘
# import sys

# def tsp(start, visited, dp):
#     # 모든 도시를 방문한 경우, 현재 위치에서 시작 도시로 가는 비용을 반환
#     if visited == (1 << n) - 1:
#         return dist[start][0] or sys.maxsize
    
#     # 이미 계산한 경우, 저장된 값을 반환
#     if dp[start][visited] != -1:
#         return dp[start][visited]
    
#     cost = sys.maxsize
    
#     # 모든 도시를 방문할 때까지 재귀 호출
#     for city in range(n):
#         if not visited & (1 << city) and dist[start][city]:
#             tmp = tsp(city, visited | (1 << city), dp) + dist[start][city]
#             cost = min(cost, tmp)
            
#     dp[start][visited] = cost
#     return cost

# # 입력
# n = int(input())
# dist = [list(map(int, input().split())) for _ in range(n)]

# # DP를 위한 메모이제이션 리스트 초기화
# dp = [[-1] * (1 << n) for _ in range(n)]

# # 출력
# print(tsp(0, 1, dp))



