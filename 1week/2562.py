# import sys
# arr = list(map(int, sys.stdin.readline().split()))

# max = arr[1]
# idx = 0
# for i in arr:
#   idx += 1
#   if max < i:
#     max = i
#     maxIdx = idx
# else:
#   print(max)
#   print(maxIdx)

import sys

arr=list(int(sys.stdin.readline()) for i in range(9) )

max_val = arr[0]
max_idx = 0

for idx, val in enumerate(arr):
    if max_val < val:
        max_val = val
        max_idx = idx

print(max_val)
print(max_idx + 1)

print(max, th, sep='\n')