# 분할 정복 (중) - 곱셈

import sys

a ,b ,c = map(int , sys.stdin.readline().split())

def pow(a, b, c):
    if b == 0:
        return 1 % c
    if b % 2 == 0:
        d = pow(a, b // 2, c)
        return (d * d) % c
    else:
        return (a * pow(a, b - 1, c)) % c

print(pow(a, b, c))