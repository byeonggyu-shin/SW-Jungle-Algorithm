# 그리디 - ATM

import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()

result = 0
lst = []
for i in p:
    if not lst:
        result += i
        lst.append(i)
    else:
        lst.append(lst[-1]+i)
        result += lst[-1]

print(result)