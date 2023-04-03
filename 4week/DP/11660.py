# dp - 구간 합 구하기 

import sys

n, m = map(int, sys.stdin.readline().split())

chart = [[0] * (n+1)]

for _ in range(n):
    chart.append([0] + list(map(int, sys.stdin.readline().split())))

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def section(x1, y1, x2, y2):

    dp = [[0] * (n+1) for _ in range(n+1)]

    # result = 0

    for i in range(y1, y2+1):
        # sum을 dp 에 저장하는 식으로 하면 될듯?
        # 마지막에 한번에?
        # result += sum(chart[i][x1:x2+1])
        # 뭔 짓 때문에 시간이 초과 될까요?
        # 1024 * 1024를 이중for로 돌리니 이럴듯
        # 한줄로 2차원 dp를 순회하는건 안될테니 dp를 1차원으로 만들고?
        for j in range(x1, x2+1):
            dp[i][j] = chart[j][i] + dp[i-1][j]

    return(dp[y2])  
    # return result

for i in range(m):
    x1, y1, x2, y2 = lst[i]
    print(sum(section(x1, y1, x2, y2)))


# ___________________________

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
        
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)