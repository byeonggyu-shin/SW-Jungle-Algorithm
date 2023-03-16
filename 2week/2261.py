# 분할 정복 (상) - 가장 가까운 두 점

# x좌표를 기준으로 점들을 정렬합니다.
# 분할 정복을 사용하여 왼쪽 부분과 오른쪽 부분에서 가장 가까운 두 점을 각각 찾습니다.
# 두 부분 중 가장 가까운 두 점을 찾습니다. 이때, 가운데 영역 내의 점들만 고려하면 됩니다.
# 2번과 3번에서 찾은 가장 가까운 두 점 중 거리가 더 작은 값을 반환합니다.

import sys
import math

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def closest(left, right, d):
    if len(left) == 1:
        return left[0], right[0], dist(left[0], right[0])

    mid_x = (left[-1][0] + right[0][0]) // 2

    left_idx = len(left) - 1
    right_idx = 0
    min_d = d

    while left_idx >= 0 and mid_x - left[left_idx][0] < min_d:
        i = left_idx
        while i >= 0 and left[i][0] == left[left_idx][0]:
            d = dist(left[left_idx], left[i])
            if d < min_d:
                min_d = d
            i -= 1
        left_idx = i

    while right_idx < len(right) and right[right_idx][0] - mid_x < min_d:
        i = right_idx
        while i < len(right) and right[i][0] == right[right_idx][0]:
            d = dist(right[right_idx], right[i])
            if d < min_d:
                min_d = d
            i += 1
        right_idx = i

    mid = (left[-1][0] + right[0][0]) // 2
    mid_points = [p for p in left + right if abs(mid - p[0]) < min_d]
    mid_points.sort(key=lambda x: x[1])

    for i in range(len(mid_points)):
        for j in range(i+1, len(mid_points)):
            if (mid_points[j][1] - mid_points[i][1])**2 > min_d:
                break
            d = dist(mid_points[i], mid_points[j])
            if d < min_d:
                min_d = d

    return min_d

n = int(sys.stdin.readline().rstrip())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort()
# print(math.sqrt(closest(points[:n//2], points[n//2:], sys.maxsize)))
print(closest(points[:n//2], points[n//2:], sys.maxsize))