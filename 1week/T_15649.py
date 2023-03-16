# from itertools import permutations
# # import itertools

# n , m = map(int, input().split())

# # lst =list(itertools.permutations(range(1,n+1),m))
# lst =list(permutations(range(1,n+1),m))
# for i in lst:
#   print(' '.join(map(str, i)))



def dfs(cur, n, m, lst, res):
    if len(cur) == m:
        res.append(cur[:])
        return

    for i in range(n):
        if lst[i] in cur:
            continue
        cur.append(lst[i])
        dfs(cur, n, m, lst, res)
        cur.pop()

n, m = map(int, input().split())
lst = list(range(1, n+1))
res = []
dfs([], n, m, lst, res)
for r in res:
    print(' '.join(map(str, r)))