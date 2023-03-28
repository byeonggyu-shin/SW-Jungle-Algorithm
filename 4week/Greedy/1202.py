# 그리디 - 보석 도둑

import sys, heapq

n, k = map(int, sys.stdin.readline().split())
jewelry = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

sorted_jewelry = sorted(jewelry, key=lambda x: x[0])
sorted_bags = sorted(bags)

lst = []
result = 0

for bag in sorted_bags :
    while sorted_jewelry and bag  >= sorted_jewelry[0][0]:
        heapq.heappush(lst, -sorted_jewelry[0][1])
        heapq.heappop(sorted_jewelry)
    
    if lst:
        result += heapq.heappop(lst)
    elif not sorted_jewelry:
        break

print(-result)


