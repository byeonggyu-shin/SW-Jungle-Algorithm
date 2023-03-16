#  이진 탐색 

def binary_search(arr, target):
    # 리스트의 양쪽 끝 인덱스를 초기화합니다.
    left = 0
    right = len(arr) - 1

    while left <= right:
        # 중간 인덱스를 찾습니다.
        mid = (left + right) // 2

        # 찾으려는 값이 중간 값과 같으면 바로 반환합니다.
        if arr[mid] == target:
            return mid

        # 찾으려는 값이 중간 값보다 작으면 왼쪽 절반을 다시 탐색합니다.
        elif arr[mid] > target:
            right = mid - 1

        # 찾으려는 값이 중간 값보다 크면 오른쪽 절반을 다시 탐색합니다.
        else:
            left = mid + 1

    # 리스트에 찾으려는 값이 없으면 None을 반환합니다.
    return None

#  

이진 탐색 

왼쪽과 오른쪽 선택 <= 배열의 양끝이 되는 경우가 많음

반복문으로 왼쪽과 오른쪽이 만나는 순간
중간값은 왼쪽, 오른쪽의 중간값 <= 리스트의 중간 인덱스 값이 되는 경우가 많음
찾는 답이 미드 값이면 미드 값을 출력
미드 값이 크다면 큰쪽인 오른쪽을 한칸 당기고
작다면 작은 쪽인 왼쪽을 한칸 당기고 다시 반복
=> 끝날떄까지 반복해서 답을 찾는다.

import sys

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

nums.sort()
result = []

for target in lst:
    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target)
    count = upper - lower
    result.append(count)

print(*result, sep=' ')