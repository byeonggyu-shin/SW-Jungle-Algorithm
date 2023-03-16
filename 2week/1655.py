#  우선순위 큐 (중) - 가운데를 말해요

import sys
import heapq

n = int(sys.stdin.readline())

max_heap = []  # 최대 힙
min_heap = []  # 최소 힙

for _ in range(n):
    num = int(sys.stdin.readline())
    # 최대 힙의 크기는 최소 힙의 크기와 같거나, 하나 더 큽니다.
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))  # 최대 힙에 값 추가
    else:
        heapq.heappush(min_heap, (num, num))  # 최소 힙에 값 추가
        
    # 최대 힙의 루트 노드가 최소 힙의 루트 노드보다 큰 경우, 값을 교환합니다.
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))
        
    # 중간값 출력
    print(max_heap[0][1])
