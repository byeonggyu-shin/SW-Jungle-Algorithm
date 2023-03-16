import sys
n = int(sys.stdin.readline())
count = 1
while count <= 9: 
  print(f"{n} * {count} = {n*count}")
  count +=1