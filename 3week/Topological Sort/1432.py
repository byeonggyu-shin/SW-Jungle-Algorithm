# 위상정렬 - 그래프 수정

# 위상 정렬 알고리즘을 사용하여 정점의 순서를 구합니다.
# 정점의 순서를 구하는 동안 다음과 같은 조건을 확인합니다:
# 그래프가 순환 구조를 가지고 있다면, -1을 출력하고 종료합니다.
# 각 정점에 대해 모든 인접한 정점의 번호가 자신보다 크다면, 그래프의 번호를 수정할 수 없습니다. 따라서 -1을 출력하고 종료합니다.
# 위상 정렬을 통해 얻은 정점 순서를 출력합니다.

import sys                               
from collections import deque

def topological_sort(n, adj_matrix):
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            in_degree[j] += adj_matrix[i][j]

    result = []
    queue = deque()

    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for i in range(n):
            if adj_matrix[current][i]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

    if len(result) != n:
        return None

    return result


n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

sorted_vertices = topological_sort(n, adj_matrix)

if sorted_vertices is None:
    print(-1)
else:
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[sorted_vertices[j]][sorted_vertices[i]]:
                print(-1)
                sys.exit()

    print(" ".join(map(lambda x: str(x + 1), sorted_vertices)))