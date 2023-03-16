import sys 

n = int(sys.stdin.readline())

count = 0
for i in range(1 , n+1):
  if i < 100:
    count += 1
  elif i <= 1000:
    a = i // 100
    b = (i // 10)%10
    c = i % 10  
    if ( a - b) == (b - c):
      count += 1
      
print(count)
# print(len(count))

 
# def is_han_number(n):
#     """
#     n이 한수인지 판별하는 함수.
#     """
#     if n < 100:
#         return True
#     else:
#         diff = int(str(n)[1]) - int(str(n)[0])
#         for i in range(2, len(str(n))):
#             if int(str(n)[i]) - int(str(n)[i - 1]) != diff:
#                 return False
#         return True

# lst =[]
# for i in range(1, n+1):
#     if is_han_number(i):
#       lst.append(i) 
#       # print(i)

# print(lst)
# print(len(lst))