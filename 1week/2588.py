import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

strB = str(b)
arr = []
for i in strB:
  arr.append(i)

for i in reversed(arr):
  print(a*int(i))
print (a*b)