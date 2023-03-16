import sys
x, y, w, h = map(int, sys.stdin.readline().split())
def findShort(a,b):
  if b-a < a:min = b-a
  else: min=a 
  return min
if findShort(x,w) > findShort(y,h): print( findShort(y,h))
else: print(findShort(x,w))