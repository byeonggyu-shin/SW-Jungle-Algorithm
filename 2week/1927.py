# 우선순위 큐 - 최소 힙

import sys
import heapq

n = int(sys.stdin.readline())

lst = []

heapq.heapify(lst)

for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst))
    else: