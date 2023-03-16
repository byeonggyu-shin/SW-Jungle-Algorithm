# import sys

# def find_nearest(hunter, targets, max_range):
#     left, right = 0, len(targets) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         dist = abs(targets[mid] - hunter)

#         if dist <= max_range:
#             return mid
#         elif targets[mid] < hunter:
#             left = mid + 1
#         else:
#             right = mid - 1

#     if left == len(targets):
#         return left - 1
#     elif right == -1:
#         return 0
#     else:
#         if abs(targets[left] - hunter) < abs(targets[right] - hunter):
#             return left
#         else:
#             return right


# M, N, L = map(int, sys.stdin.readline().split())
# hunters = sorted(list(map(int, sys.stdin.readline().split())))

# count = 0
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().split())

#     nearest_hunter = find_nearest(x, hunters, L)
#     if abs(x - hunters[nearest_hunter]) + y <= L:
#         count += 1

# print(count)



import sys

# 이분 탐색 함수 => 사대를 이분 탐색해서 타겟과 가장 가까운 사대를 찾음 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

m, n, l = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
s.sort()  # 사대를 x좌표 기준으로 오름차순 정렬

animals = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if y <= l:  # 사정거리 이내인 동물만 처리
        animals.append((x, y))

animals.sort(key=lambda x: x[1])  # 동물을 y좌표 기준으로 오름차순 정렬

cnt = 0  # 잡을 수 있는 동물의 수
for x, y in animals:
    # 이분 탐색을 수행하여 사대 중 가장 가까운 위치를 찾습니다.
    idx = binary_search(s, x)
    
    # idx-1, idx, idx+1 중에서 동물과 가장 가까운 사대를 선택합니다.
    dist1 = abs(x - s[idx-1]) + y if idx-1 >= 0 else sys.maxsize
    dist2 = abs(x - s[idx]) + y if idx < m else sys.maxsize
    dist3 = abs(x - s[idx+1]) + y if idx+1 < m else sys.maxsize
    
    # 가장 가까운 사대와의 거리가 사정거리 이내라면, 동물을 잡을 수 있습니다.
    if min(dist1, dist2, dist3) <= l:
        cnt += 1

print(cnt)