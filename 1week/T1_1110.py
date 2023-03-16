import sys 

n = int(sys.stdin.readline())

lst = [n]
    
# while True:
#   i = lst[-1]
#   plus = i//10 + i%10
#   cycle = (i%10)*10 + plus%10
#   if cycle == lst[0]:
#       print(len(lst))
#       break
#   lst.append(cycle)
#   if len(lst) >= 101:
#       break
       

for _ in lst:
  i = lst[-1]
  plus = i//10 + i%10
  cycle = (i%10)*10 + plus%10
  if cycle == lst[0]:
      print(len(lst))
      break
  lst.append(cycle)
  if len(lst) >= 101:
      break
         
# def findCyle(i):  
#     global lst 
#     plus = i//10 + 1%10
#     if plus < 10:
#         cycle = i%10 + plus
#     else:
#         cycle = i%10 + plus//10 
#     if cycle == lst[0]:
#         return len(lst)
#     lst.append(cycle)
#     return findCyle(cycle)

