# 그리디 - ATM

import sys

def toggle_matrix(matrix, x, y):
    for i in range(3):
        for j in range(3):
            matrix[x + i][y + j] = 1 - matrix[x + i][y + j]

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

operations = 0

for x in range(n - 2):
    for y in range(m - 2):
        if a[x][y] != b[x][y]:
            toggle_matrix(a, x, y)
            operations += 1

if a == b:
    print(operations)
else:
    print(-1)