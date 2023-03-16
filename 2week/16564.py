import sys

n , k = map(int, sys.stdin.readline().split())
player_lv = []
for _ in range(n):
    player_lv.append(int(sys.stdin.readline()))
player_lv.sort()

min_lv = min(player_lv)
max_lv = min(player_lv) + k

while min_lv < max_lv:
    mid_lv = (min_lv + max_lv + 1) // 2
    total_increase = sum(max(0, mid_lv - lv) for lv in player_lv)
    
    if total_increase > k:
        max_lv = mid_lv - 1
    else:
        min_lv = mid_lv

print(min_lv)


# 리스트에 최소 값을 중간 값까지 올리고 
# 2개의 값에 하나씩 최고 점까지 올리고
# 3개가 같아지면 3개씩 올리면 

import sys
n, k = map(int, input().split())
levels = [int(sys.stdin.readline()) for _ in range(n)]

levels.sort()
left, right = levels[0], levels[-1] + k

def get_diff(mid):
    diff = 0
    for level in levels:
        if level < mid:
            diff += mid - level
        else:
            break
    return diff


while left <= right:
    mid = (left + right) // 2
    diff = get_diff(mid)
    if diff <= k:
        left = mid+1
    else:
        right = mid - 1

print(right)

첫 번째 코드에서는 T 값을 이분 탐색하면서, T 값 이하의 모든 레벨을 T 값으로 만들기 위해 필요한 레벨 증가량을 계산합니다. 이 증가량의 총합이 K보다 작으면, T 값을 더 큰 값으로 옮겨서 적어도 K 이상의 레벨 증가량을 얻을 수 있도록 합니다. 이 방식은 이분 탐색을 수행하는 동안 계속해서 레벨 증가량을 계산해야 하므로, 시간 복잡도가 높아집니다.

두 번째 코드에서는 이분 탐색을 수행하면서, T 값을 이용하여 레벨 증가량을 직접 계산합니다. 이분 탐색을 수행하는 동안 계속해서 레벨 증가량을 계산하는 것이 아니라, 이 값만 계산하면 되므로 시간 복잡도가 낮아집니다.

또한 두 코드의 구현 방식도 약간 차이가 있습니다. 첫 번째 코드에서는 T 값을 이분 탐색할 때, while 반복문의 조건식에서 left < right가 아니라 left <= right를 사용합니다. 이는 T 값이 최댓값일 때, T 값을 옮기기 전에 먼저 T 값을 찾아서 반환해야 하기 때문입니다. 반면에 두 번째 코드에서는 right 변수를 반환하기 때문에, left < right 조건식을 사용할 수 있습니다.