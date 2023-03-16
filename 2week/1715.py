#  우선순위 큐 (중) - 카드 정렬하기

import sys
import heapq

n = int(sys.stdin.readline())

cards = []
for _ in range (n):
    heapq.heappush(cards, int(sys.stdin.readline()))

count = 0

while len(cards) > 1:
    bundle_card = heapq.heappop(cards)
    bundle_card += heapq.heappop(cards)
    count +=  bundle_card 
    heapq.heappush(cards, bundle_card)

print(count)