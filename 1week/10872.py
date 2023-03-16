import sys
sys.setrecursionlimit(10**6)

def fec(x):
    if x <= 1:
      return 1
    else:
      return x*fec(x-1)
n = int(sys.stdin.readline())
result = fec(n)
print(result)