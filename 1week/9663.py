# import sys 
# n = int(sys.stdin.readline())

# def solveNQueens(n):
#     def backtrack(board, row):
#         if row == n:
#             res.append(board)
#             return
#         for col in range(n):
#             if col in cols or row-col in diag1 or row+col in diag2:
#                 continue
#             cols.add(col)
#             diag1.add(row-col)
#             diag2.add(row+col)
#             backtrack(board+[(row,col)], row+1)
#             cols.remove(col)
#             diag1.remove(row-col)
#             diag2.remove(row+col)

#     res = []
#     cols, diag1, diag2 = set(), set(), set()
#     backtrack([], 0)
#     return len(res)

# print(solveNQueens(n))


import sys
def logic(n):
    if n == N: 
        global count 
        count += 1 
    else:
        for i in range(N):
            if visited[i]:
                continue
            board[n] = i 
            if check(n): 
                visited[i] = True
                logic(n+1) 
                visited[i] = False
def check(n):
    for i in range(n):
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False
    return True
N = int(sys.stdin.readline())
count = 0   
board = [0 for _ in range(N)] 
visited = [False for _ in range(N)]
logic(0)
print(count)