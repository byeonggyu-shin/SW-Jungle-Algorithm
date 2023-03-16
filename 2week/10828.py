import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    m  = list(sys.stdin.readline().split())
    
    if len(m) == 1:
        i = m[0]
    else:
        i , j = m[0] ,m[1]
    
    if i == 'push':
        lst.append(j)
    if i == 'pop':
        if len(lst) == 0:
            print (-1)
        else:
          print(lst[-1])    
          del lst[-1]
    if i == 'size':
        print(len(lst))
    if i == 'empty':
        if len(lst) == 0:
            print (1)
        if len(lst) != 0:
            print (0)
    if i == 'top':
        if len(lst) == 0:
            print (-1)
        if len(lst) != 0:
            print (lst[-1])