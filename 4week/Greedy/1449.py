# 그리디 - 수리공 항승

import sys

n, l = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))

p.sort()

tape = 0
cnt = 0

for i in p:
    if tape > i:
        continue
    else:
        tape = i +l        
        cnt += 1

print(cnt)