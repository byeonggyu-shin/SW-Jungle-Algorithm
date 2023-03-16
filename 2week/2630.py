# 분할 정복 (하) - 색종이 자르기

import sys

n = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

w_cnt, b_cnt = 0, 0

def cut_paper(n, x, y):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if lst[i][j]:
                tmp_cnt += 1

    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == n**2:
        b_cnt += 1
    else:
                # 분할하여 재귀적으로 해결합니다.
        cut_paper(n//2, x, y)
        cut_paper(n//2, x, y+n//2)
        cut_paper(n//2, x+n//2, y)
        cut_paper(n//2, x+n//2, y+n//2)
    # 만약 해당 영역의 모든 색이 같다면 해당 색으로 색종이를 자릅니다.
    return 

cut_paper(n, 0, 0)
print(w_cnt)
print(b_cnt)



# import sys

# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# result = []

# def solution(x, y, N) :
#   color = paper[x][y]
#   for i in range(x, x+N) :
#     for j in range(y, y+N) :
#       if color != paper[i][j] :
#         solution(x, y, N//2)
#         solution(x, y+N//2, N//2)
#         solution(x+N//2, y, N//2)
#         solution(x+N//2, y+N//2, N//2)
#         return
#   if color == 0 :
#     result.append(0)
#   else :
#     result.append(1)


# solution(0,0,N)
# print(result.count(0))
# print(result.count(1))