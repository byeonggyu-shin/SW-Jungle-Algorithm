# 이분 탐색 - 랜선 자르기

# import sys

# k ,n =map(int ,sys.stdin.readline().split())

# lst = [int(sys.stdin.readline()) for _ in range(k)]

# lst.sort()

# max_length = sum(lst) // n
# min_length = lst[-1] // n

# while min_length <= max_length:
#     mid = (max_length+min_length)//2

#     cnt = 0
#     for i in lst:
#         cnt += i//mid
#     if cnt == n:
#         mid
#     elif  cnt >= n:
#         min_length = mid + 1
#     else:
#         max_length = mid - 1




import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

min_length = 1
# 랜선들 중 가장 긴 랜선의 길이 => 이진 탐색에서 사용할 최대 값
max_length = max(lines)
result = 0

while min_length <= max_length:
    # 최소 값과 최대 값의 중간 값
    mid = (min_length + max_length) // 2
    # 주어진 랜선들을 mid 길이로 잘랐을 때 얻을 수 있는 랜선 개수를 계산
    total_lines = sum(line // mid for line in lines)

    if total_lines >= N:
        result = mid
        min_length = mid + 1
    else:
        max_length = mid - 1
    #  최소 값이 최대 값보다 작거나 같을 때까지 반복
print(result)