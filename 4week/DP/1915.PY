# DP - 가장 큰 정사각형

import sys

n, m = map(int, sys.stdin.readline().split())

lst = [list(sys.stdin.readline().split().strip()) for _ in range(m)]

matrix = [input() for _ in range(n)]

dp = [[0] * m for _ in range(n)]
max_size = 0

for i in range(n):
    for j in range(m):
        
        if i == 0 or j == 0:
            
            dp[i][j] = int(matrix[i][j])

        else:
            
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

            else:
                dp[i][j] = 0

        max_size = max(max_size, dp[i][j])

print(max_size ** 2)