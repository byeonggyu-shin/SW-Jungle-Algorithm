# 이진 탐색 - k번째 수

# # 메모리 초과
# import sys

# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline())

# lst = [[0]* n for _ in range(n)]


# for idx1 ,i in enumerate(lst):
#   for idx2 ,j in enumerate(lst):
#       lst[idx1][idx2] = (idx1+1)*(idx2+1)

# cut , rest = divmod(k,n)

# print(lst[cut][rest])


import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 최소 값은 1로 설정
min_val = 1
# 최대 값은 N * N 배열상 최대값
max_val = N * N
result = 0

# 이진 탐색
while min_val <= max_val:
    # 최소 값과 최대 값의 중간 값
    mid = (min_val + max_val) // 2

    # NxN 배열에서 mid보다 작거나 같은 수의 개수를 계산
    count = sum(min(mid // i, N) for i in range(1, N + 1))

    if count >= K:
        # mid보다 작거나 같은 수의 개수가 K 이상이면, 최대 값을 mid - 1로 업데이트 
        # 결과 값을 mid로 저장
        result = mid
        max_val = mid - 1
    else:
        # mid보다 작거나 같은 수의 개수가 K 미만이면, 최소 값을 mid + 1로 업데이트
        min_val = mid + 1
    # 최소 값이 최대 값보다 작거나 같을 때까지 위 과정을 반복
print(result)