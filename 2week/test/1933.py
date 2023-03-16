import sys
import heapq 

n = int(sys.stdin.readline())

building = []

for _ in range(n):
    building.append(list(map(int, sys.stdin.readline().split())))

building.sort()
# 정렬하고 가장 높은 높이에 따라 새로운 값

# 딕셔너리로 한다면?
# 딕셔너리에 담아서 x값이 0이되는걸 찾고

# 힙으로? 

# result = []
heap = []
# 힙에다가 저장? 높이를 담아두어야하나? 

for i in building:
    start = i[0]  
    height = i[1]  
    end = i[2]  

    # 앞건물의 end와 start 비교 , 높이 비교 => 안겹치면 0
    # 크다면 start 부터 작다면 end 부터 크다면 앞건물이 넣어둔걸 뺴버리고

 