import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    h = int(sys.stdin.readline())

    if len(lst) == 0:
        lst.append(h)
    elif lst[-1] < h:
        for i in lst[::-1]:
            if i <= h:
                lst.pop()
        lst.append(h)
    elif lst[-1] > h:
        lst.append(h)
    
print(len(lst))