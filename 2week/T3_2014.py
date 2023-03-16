# 우선순위 큐 - 소수의 곱 

import sys
import heapq

K, N = map(int, sys.stdin.readline().split())
primes = list(map(int, sys.stdin.readline().split()))
# 우선순위 큐에 소수들을 삽입합니다.
pq = primes[:]
heapq.heapify(pq)

# 중복을 방지하기 위해 이미 처리한 소수 곱을 저장하는 집합을 생성합니다.
visited = set(primes)

for _ in range(N - 1):
    min_val = heapq.heappop(pq)  # 가장 작은 수를 추출합니다.

    for prime in primes:
        mul = min_val * prime

        # 이미 처리한 소수 곱이 아닌 경우만 삽입하고, 집합에 추가합니다.
        if mul not in visited:
            visited.add(mul)
            heapq.heappush(pq, mul)

        # min_val에 가장 큰 소수를 곱한 값이 더 이상 필요하지 않으면 반복문을 종료합니다.
        if min_val % prime == 0:
            break

# N번째로 추출한 수가 정답입니다.
print(heapq.heappop(pq))

# K개의 소수를 입력 받습니다.
# 우선순위 큐(priority queue)를 생성하고, 입력 받은 소수들을 삽입합니다.
# N번째 소수 곱을 찾을 때까지 다음을 반복합니다:
# a. 우선순위 큐에서 가장 작은 수(최소 힙)를 추출합니다.
# b. 추출한 수에 각 소수를 곱하여 다시 우선순위 큐에 삽입합니다.
# c. 이미 처리한 소수 곱은 다시 처리하지 않도록 주의합니다.
# N번째로 추출한 수가 정답입니다.
