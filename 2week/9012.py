import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = sys.stdin.readline().strip()
    lst = []
    for i in n:
        if i == '(':
            lst.append(i)    
        elif lst and lst[-1] == '(':
            lst.pop()
        else:
            lst.append(i)        
    if not lst: 
        print('Yes')
    else:
        print('NO')

