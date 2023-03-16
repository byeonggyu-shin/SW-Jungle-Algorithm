import sys

n = int(sys.stdin.readline())

liquids = sorted(list(map(int, sys.stdin.readline().split())))

temp = float('inf')
result = []
# left ,right = 0 , -1
for i in range(n):
    left = i + 1
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        diff = liquids[i] + liquids[mid]
        if abs(diff) < temp:
            temp = abs(diff)
            result = [liquids[i], liquids[mid]]
        if diff < 0:
            left = mid + 1
        elif diff > 0:
            right = mid - 1
        else:
            break
print(result[0], result[1])
  
# 용액 리스트에서 첫번째 용액과 마지막 용액의 idx를 left = i-1 , right = n-1 값으로 설정하고
#  mid = (left + right) // 2 로 설정

import sys
input = sys.stdin.readline

N = int(input())
solution = sorted(list(map(int, input().split())))

left = 0
right = N-1
result = [float('inf'), left, right]
while left < right:
    mixture = solution[left] + solution[right]
    if mixture == 0:
        # print(left, right)
        # sys.exit()
        result = [0, left, right]
        break
    elif mixture < 0:
        if abs(mixture) < abs(result[0]):
            result = [mixture, left, right]
        left += 1
    else:
        if abs(mixture) < abs(result[0]):
            result = [mixture, left, right]
        right -= 1
print(solution[result[1]], solution[result[2]])