# 분할 정복 (중) - 행렬 제곱

import sys
# 행렬의 크기 N과 B
n,b = map(int , sys.stdin.readline().split())

A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= 1000
    return C

def power(A, B):
    if B == 1:
        for i in range(n):
          for j in range(n):
              A[i][j] %= 1000
        return A
    elif B % 2 == 0:
        temp = power(A, B//2)
        return multiply(temp, temp)
    else:
        temp = power(A, (B-1)//2)
        return multiply(multiply(temp, temp), A)

result = power(A, b)

for row in result:
    print(' '.join(map(str, row)))