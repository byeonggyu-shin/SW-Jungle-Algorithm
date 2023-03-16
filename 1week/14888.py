#  시간 초과 
# import sys 
# import itertools 

# n = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# opr = list(map(int, sys.stdin.readline().split()))

# opr_str = "+-*/"
# newOpr = []
# for i in range(4):
#     newOpr += opr_str[i] * opr[i]

# cases = itertools.permutations(newOpr) 

# max_val = 0
# min_val = float('inf')

# for case in cases:

#   for i in range(1,len(lst)):
#     result = lst[0] 

#     for j in range(len(case)):
#       result = int(eval(str(result)+case[j]+str(lst[j+1])))

#     if result >= max_val:
#       max_val = result
#     if result <= min_val:
#       min_val = result


# print(max_val, min_val)



import sys 

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
opr = list(map(int, sys.stdin.readline().split()))

max_val = -float('inf')
min_val = float('inf')

def dfs(idx, val, add, sub, mul, div):
    global max_val, min_val
    if idx == n:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    if add:
        dfs(idx+1, val+lst[idx], add-1, sub, mul, div)
    if sub:
        dfs(idx+1, val-lst[idx], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, val*lst[idx], add, sub, mul-1, div)
    if div:
        if val >= 0:
            dfs(idx+1, val//lst[idx], add, sub, mul, div-1)
        else:
            dfs(idx+1, -((-val)//lst[idx]), add, sub, mul, div-1)

dfs(1, lst[0], opr[0], opr[1], opr[2], opr[3])
print(max_val)
print(min_val)