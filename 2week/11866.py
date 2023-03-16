# 큐 (하) - 요세푸스 문제 0

import sys
from collections import deque

n , k = map(int, sys.stdin.readline().split())
queue = deque()
for i in range(1,n+1):
    queue.append(i)

result = []

while len(queue) >= 1:
    for _ in range(k-1):
      queue.append(queue.popleft())
    result.append(queue.popleft())
    
print('<' + ', '.join(map(str, result)) + '>')