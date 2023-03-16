# 만약 size가 1이라면, 현재 위치를 반환합니다.

# size가 1보다 크다면, 배열을 4분할해서 재귀적으로 탐색합니다.

# 좌상단 분할 영역을 탐색하기 위해서는 x, y 좌표와 현재 배열 크기의 1/2을 인자로 전달합니다.

# 좌상단 분할 영역에서 찾은 위치를 4등분한 부분 중 하나라면, 0을 반환합니다.

# 우상단 분할 영역을 탐색하기 위해서는 x, y+현재 배열 크기의 1/2, 현재 배열 크기의 1/2을 인자로 전달합니다.

# 우상단 분할 영역에서 찾은 위치를 4등분한 부분 중 하나라면, 1을 반환합니다.

# 좌하단 분할 영역을 탐색하기 위해서는 x+현재 배열 크기의 1/2, y, 현재 배열 크기의 1/2을 인자로 전달합니다.

# 좌하단 분할 영역에서 찾은 위치를 4등분한 부분 중 하나라면, 2를 반환합니다.

# 우하단 분할 영역을 탐색하기 위해서는 x+현재 배열 크기의 1/2, y+현재 배열 크기의 1/2, 현재 배열 크기의 1/2을 인자로 전달합니다.

# 우하단 분할 영역에서 찾은 위치를 4등분한 부분 중 하나라면, 3을 반환합니다.

import sys 

n ,r ,c  = list(map(int, sys.stdin.readline().split()))

def search(n, r, c, count):
    if n == 0:
        return count
    half = 2**(n-1)
    if r < half and c < half:
        return search(n-1, r, c, count)
    elif r < half and c >= half:
        return search(n-1, r, c-half, count+2**(2*n-2))
    elif r >= half and c < half:
        return search(n-1, r-half, c, count+2**(2*n-2)*2)
    else:
        return search(n-1, r-half, c-half, count+2**(2*n-2)*3)
    
print(search(n,r,c,0))
     
     