# 그리디 - 합분해

import sys

n ,k = map(int , sys.stdin.readline().split())

def div():
    dp = [[0] * n for _ in range(k)]

    for i in range(n):
        dp[0][i] = 1
    for i in range(k):
        dp[i][0] = i+1

    for i in range(k):
        for j in range(n):
            if dp[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
            else:
                continue
    return(dp[k-1][n-1])

print(div()%1000000000)

