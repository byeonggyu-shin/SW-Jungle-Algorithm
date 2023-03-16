import sys

n = int(sys.stdin.readline())
lstN = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
lstM = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] == target:
          return 1
      elif arr[mid] < target:
          left = mid + 1
      else:
          right = mid - 1
  return 0

for i in lstM:
    print(binary_search(lstN , i))



# n을 입력 받음
# 입력된 값으로 lst를 만듦

# lst.sort() 로 정렬

# 왼쪽값 오른쪽값은 lst의 양끝

# 가장 단순한 이분 탐색 알고리즘

# 반복을 통해 모든 m 리스트의 값을 이분탐색해서 한줄씩 결과 출력