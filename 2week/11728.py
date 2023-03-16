# 우선순위 큐 - 배열 합치기

import sys

n,m = map(int,sys.stdin.readline().split())

lstA = list(map(int,sys.stdin.readline().split()))
lstB = list(map(int,sys.stdin.readline().split()))

combined_lst = lstA + lstB
combined_lst.sort()
print(*combined_lst, end=' ')