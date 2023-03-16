# 1. 입력을 받고 집의 좌표를 정렬합니다.
# 2. 공유기를 설치할 수 있는 범위를 정합니다. 가장 인접한 두 공유기 사이의 거리의 최솟값은 1이고, 최댓값은 가장 먼 두 집 사이의 거리입니다.
# 3. 공유기를 설치할 수 있는 범위를 반씩 나누어서 탐색합니다.
# 4. 탐색하려는 범위 내에서 공유기를 설치할 수 있는지 확인합니다. 이를 위해서는 첫 번째 집부터 마지막 집까지 순서대로 탐색하면서, 이전에 설치한 공유기와의 거리가 현재 공유기를 설치할 수 있는 거리 이상인 경우에만 공유기를 설치합니다. 이 때, 공유기를 C개 이상 설치할 수 있는지도 확인합니다.
# 5. 공유기를 C개 이상 설치할 수 있는 경우, 탐색 범위의 최솟값을 현재 범위의 중간값으로 업데이트합니다.
# 6. 공유기를 C개 이상 설치할 수 없는 경우, 탐색 범위의 최댓값을 현재 범위의 중간값으로 업데이트합니다.
# 7. 탐색 범위가 충분히 작아질 때까지 반복합니다.
# 8. 최종적으로 탐색 범위의 최솟값이 가장 인접한 두 공유기 사이의 거리의 최대값입니다.

import sys 

N,C = map(int, sys.stdin.readline().split())

houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()

# start = houses[0] # 가능한 거리의 최솟값은 1입니다.
start = 1 # 가능한 거리의 최솟값은 1입니다.
end = houses[-1] - houses[0] # 가능한 거리의 최댓값은 첫번째 집과 마지막 집의 거리입니다.

result = 0
while start <= end:
    mid = (start + end) // 2 # 가능한 가장 인접한 두 공유기 사이의 거리입니다.
    count = 1 # 첫번째 집에는 무조건 공유기를 설치합니다.
    current_house = houses[0]
    for i in range(1, N):
        if houses[i] - current_house >= mid:
            count += 1
            current_house = houses[i]
            if count > C:
                break

    if count >= C: # 공유기의 수가 많거나 같으면 가능한 거리를 늘립니다.
        result = mid
        start = mid + 1
    else: # 공유기의 수가 적으면 가능한 거리를 줄입니다.
        end = mid - 1

print(result)