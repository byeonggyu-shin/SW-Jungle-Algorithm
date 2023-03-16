#  스택 - 쇠막대기

import sys

parenthesis_string = sys.stdin.readline()

lst = []
cnt =0

for i in range(len(parenthesis_string)):
    if parenthesis_string[i] == '(':
        if parenthesis_string[i+1] == ')':
            cnt += len(lst)
        else:
            cnt += 1    
        lst.append(parenthesis_string[i])
        
    else:
        if lst:
            lst.pop()

print(cnt)