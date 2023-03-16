import sys
import itertools

n , m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

combs = itertools.combinations(lst, 3)  

num = 0

for comb in combs:
    if sum(comb) == m :
        print (m)
        exit()
    elif sum(comb) < m and sum(comb) > num:  
        num = sum(comb)
else:
    print(num)