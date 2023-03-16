import sys
from itertools import permutations

n = int(sys.stdin.readline())
data = list('123456789')
cases = list(permutations(data, 3))

for _ in range(n):
  q , s, b = map(int,sys.stdin.readline().split())
  q = list(str(q))
  
  filted = []

  for i in range(len(cases)):
      strike = ball = 0
      for j in range(3):
          if cases[i][j] == q[j]:
              strike += 1
          elif q[j] in cases[i]:
              ball += 1
          
      if (strike == s) and (ball == b):
          filted.append(cases[i])

  cases = filted        

print(len(cases))

