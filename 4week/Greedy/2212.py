# 그리디 - 센서

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = sorted(list(map(int, sys.stdin.readline().split())))

# 최소가 되도록 영역을 k개로 나누면 된다.

# 센서가 더 많다면 0출력
if k >= n:
    print(0)
else:
    # 인접한 센서 위치 간의 차이를 계산
    diff = [sensors[i] - sensors[i - 1] for i in range(1, n)]
    # 내림차순으로 정렬
    diff.sort(reverse=True)
    
    total_removed_gaps = sum(diff[:k - 1])

    # 원래 전체 영역에서 (양끝 값) 에서 끊은 영역 합을 뺴줌
    result = sensors[-1] - sensors[0] - total_removed_gaps
    print(result)

