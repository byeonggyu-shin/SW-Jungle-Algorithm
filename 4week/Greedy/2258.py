# 그리디 - 정육점

import sys

def getMinCost(meats):

    weightCount = 0
    sameCostCount = 0
    costList = []

    for i in range(n):
        w, c = meats[i]

        weightCount += w
        # 1. 같은 가격인 고기들을 여러 개 살 경우
        if i >= 1 and c == meats[i-1][1]:
            sameCostCount += c
        # 2. 일반적인 경우, 이전 고기보다 현재 고기가 비쌀 경우
        else:
            sameCostCount = c

        if weightCount >= m:
            costList.append(sameCostCount)

            # 2의 경우인데 목표 중량을 달성했을 경우에는 더이상 반복문을 돌릴 필요가 없음
            if sameCostCount == c:
                break

    if costList:
        return min(costList)
    else:
        return -1

n, m = map(int, sys.stdin.readline().split())

meats = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], -x[0]))

print(getMinCost(meats))