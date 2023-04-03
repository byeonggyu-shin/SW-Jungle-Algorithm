# 그리디 - ATM

import sys
 
t = int(sys.stdin.readline())

def stock():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    max_p = 0
    total_p = 0

    for i in reversed(p):
        if i > max_p:
            max_p = i
        else:
            total_p += max_p - i

    return(total_p)

for _ in range(t):
    print(stock())