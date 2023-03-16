# 큐 - 큐

import sys

n = int(sys.stdin.readline())

lst=[]
for _ in range(n):
    m = list(sys.stdin.readline().split())
    if len(m) == 1:
        if len(lst) == 0:
            if m[0] == 'size':
                print(0)
            elif m[0] == 'empty':
                print(1)    
            else:
                print(-1)
        elif m[0] == 'front':
            print(lst[0])
        elif m[0] == 'pop':
            print(lst[0])
            del lst[0]
        elif m[0] == 'size':
            print(len(lst))
        elif m[0] == 'empty':
            print(0)
        elif m[0] == 'back':
            print(lst[-1])
    else:
        lst.append(m[1])                       