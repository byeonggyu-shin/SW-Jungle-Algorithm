import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
mlt = a * b * c

lst = [0] * 10
for i in str(mlt):
  lst[int(i)] += 1

for i in lst:
  print(i)     
