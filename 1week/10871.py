import sys
n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = []
for i in arr:
    if i < x:
        result.append(str(i))  
print(' '.join(result))
