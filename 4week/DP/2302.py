# DP - 극장 좌석

import sys 

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

fixed = [int(sys.stdin.readline()) for _ in range(m)]

def rule(n):
    if n == 1:
        return 1
    elif n == 2: 
        return 2
    else:
        return rule(n-1) + rule(n-2)

dp = [ i for i in range(1,n+1)]


area = dp[:fixed[0]-1]
result = rule(len(area))

for j in range(m):
    if j == m-1:
        area = dp[fixed[j]:]
        result *= rule(len(area))
    else:
        area = dp[fixed[j]:fixed[j+1]-1]
        result *= rule(len(area))

print(result)