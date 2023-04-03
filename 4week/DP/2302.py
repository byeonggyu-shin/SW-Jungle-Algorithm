# DP - 극장 좌석

import sys 
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

fixed = [int(sys.stdin.readline()) for _ in range(m)]

def rule(n, memo):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif memo[n] != 0:
        return memo[n]
    else:
        memo[n] = rule(n - 1, memo) + rule(n - 2, memo)
        return memo[n]

memo = [0] * (n + 1)

dp = [ i for i in range(1,n+1)]

area = dp[:fixed[0]-1]
result = rule(len(area), memo)

if m != n:
    for j in range(m):
        if j == m-1:
            area = dp[fixed[j]:]
            result *= rule(len(area))
        else:
            area = dp[fixed[j]:fixed[j+1]-1]
            result *= rule(len(area))
    else:
        print(result)
else:
    print(1)

________________

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = [int(sys.stdin.readline()) for _ in range(m)]

dp = [0] * (n + 2)
dp[0] = 1
dp[1] = 1 
dp[2] = 2 
# 점화식 : dp[n] = dp[n - 1] + dp[n - 2]
for i in range(3, n+2):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1 # 경우의 수
# vip의 유무에 따라 경우의 수를 도출
if m > 0:
    pre = 0
    # 반복문을 통해 vip 사이에 그룹에 들어가는 경우의 수를 확인
    for j in range(m):
        answer *= dp[vip[j] - 1 - pre]
        pre = vip[j]
    answer *= dp[n - pre]
else:
    answer = dp[n]
print(answer)

___________
