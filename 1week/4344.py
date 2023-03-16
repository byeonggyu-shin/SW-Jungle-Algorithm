import sys

c = int(sys.stdin.readline())

for _ in range(c):
  test = list(map(int, sys.stdin.readline().split()))
  sum = 0
  for i in range(1, test[0]+1):
    sum += test[i]
  avg = sum / test[0]
  count = 0
  for i in range(1, test[0]+1):
    if test[i] > avg:
      count += 1
  print(f"{count/test[0]*100:.3f}%") 
  

# import sys

# c = int(sys.stdin.readline())

# for i in range(c):
#     test = list(map(int, sys.stdin.readline().split()))
#     n = test[0]
#     scores = test[1:]
#     avg = sum(scores) / n
#     count = sum(1 for score in scores if score > avg)
#     ratio = count / n * 100
#     print(f"{ratio:.3f}%")
