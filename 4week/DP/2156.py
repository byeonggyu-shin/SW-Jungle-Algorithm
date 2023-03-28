# DP - 포도주 시식

import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (n + 1)
# 1번은 무조건 먹어야하는 경우
dp[1] = wine[1]

if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    # i-2 잔을 건너 뛸지 , i-1 잔을 건너뛸지  , i 잔을 건너뛸지 점화식으로 판단
    dp[i] = max(dp[i - 3] + wine[i - 2] + wine[i -1], dp[i - 2] + wine[i-1], dp[i - 1])

print(dp[n])