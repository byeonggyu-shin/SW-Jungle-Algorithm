# DP (하) - 01타일

import sys

def tile(n):
    
    a = [0] * (n+1)
    
    a[1] = 1
    a[2] = 2

    for i in range(3, n+1):
         a[i] = (a[i-1] + a[i-2]) % 15746

    return a[n]     

n = int(sys.stdin.readline())

print(tile(n))