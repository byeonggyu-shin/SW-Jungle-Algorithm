# 이분 탐색 - 숫자 카드 2

# import sys

# n = int(sys.stdin.readline())
# nums = list(map(int , sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# lst = list(map(int , sys.stdin.readline().split()))

# def binary_search(target):
#     left , right = 0 , len(nums)-1
#     while left <= right:
#         mid = (left +right) // 2
#         if nums[mid] == target:
#             nums.remove(nums[mid])
#             return 1
#         elif nums[mid] > target:
#             right = mid -1 
#         else:
#             left = mid + 1 
#     return 0

# nums.sort()
# result = [0] * m

# for idx, i in enumerate(lst):
#     cnt = 0
#     while binary_search(i):
#         cnt += 1
#     result[idx] = cnt        

# print (*result, sep=' ')

# 이진 탐색 + 도수 정렬 문제 

# nums 리스트 정렬 
# 이진 탐색 함수 제작 
# m 길이 만큼의 0이 들어간 결과 리스트를 만들고
# lst를 반복해서 이진 탐색함수에 모든 결과를 넣고 
# 결과값으로 t,f 판별후 결과리스트의 해당 인덱스 값을 1씩 증가.

# def binary_search(nums, target):
#     # 중복된 값이 있는 경우 첫 번째 등장하는 인덱스를 찾는 함수
#     def find_first_index(nums, target):
#         left, right = 0, len(nums)-1
#         first_index = -1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] >= target:
#                 right = mid - 1
#                 if nums[mid] == target:
#                     first_index = mid
#             else:
#                 left = mid + 1
#         return first_index

#     # 중복된 값이 있는 경우 마지막 등장하는 인덱스를 찾는 함수
#     def find_last_index(nums, target):
#         left, right = 0, len(nums)-1
#         last_index = -1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] <= target:
#                 left = mid + 1
#                 if nums[mid] == target:
#                     last_index = mid
#             else:
#                 right = mid - 1
#         return last_index

#     # 중복된 값이 있는 경우, 첫 번째 등장하는 인덱스와 마지막 등장하는 인덱스를 찾아서 등장 횟수를

import sys
# n개의 숫자를 입력
n = int(sys.stdin.readline())
dic = {}
# dic이라는 딕셔너리를 만들어 각 숫자의 개수를 저장
# 입력받은 숫자들을 분리하여 dic에 저장하거나 개수를 증가
for s in sys.stdin.readline().split():
    if dic.get(s) != None:
        dic[s] += 1
    else:
        dic[s] = 1
m = int(sys.stdin.readline())
# 입력받은 타겟 숫자들에 대해 개수를 찾아 출력
# 만약 숫자가 dic에 없다면, 0을 출력
for s in sys.stdin.readline().split():
    if dic.get(s) != None:
        print(dic.get(s), end=" ")
    else:
        print(0, end=" ")