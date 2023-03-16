#  우선순위 큐 (중) - 철로

import sys
import heapq

n = int(sys.stdin.readline())
people = []
for i in range(n):
    people.append(list(map(int , sys.stdin.readline().split())))
    people[i].sort()
d = int(sys.stdin.readline())

rail = []
cnt = 0
# D 이하인 기차만 리스트
for road in people:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        rail.append(road)
rail.sort(key=lambda x:x[1])

heap = []
for road in rail:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    cnt = max(cnt, len(heap))

print(cnt)




# import sys
# import heapq
# input = sys.stdin.readline

# human_num = int(input())
# house_office = [sorted(list(map(int,input().split())))for _ in range(human_num)]
# dis_max = int(input())
# target = []
# heap = []

# for i in house_office:
#     if i[1]-i[0] <= dis_max:
#         target.append(i)
# target.sort(key=lambda x:x[1])
# answer = 0
# for i in target:
#     if not heap:
#         heapq.heappush(heap, i)
#     else:
#         while heap[0][0] < i[1]-dis_max:
#             heapq.heappop(heap)
#             if not heap:
#                 break
#         heapq.heappush(heap, i)
#     answer = max(answer, len(heap))
# print(answer)