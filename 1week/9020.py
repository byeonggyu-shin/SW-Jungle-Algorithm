import sys 
n = int(sys.stdin.readline())

def is_prime(n):
  if n == 1:
    return False
  if n == 2 or n == 3:
      return True
  if n % 2 == 0 or n % 3 == 0:
      return False
  for i in range(5, int(n**0.5)+1, 6):
      if n % i == 0 or n % (i+2) == 0:
          return False
  return True
  
for _ in range(n):
  a = int(sys.stdin.readline())

  for x in list(range(1, int(a/2+1)))[::-1]:
    if is_prime(x):
      if is_prime(a - x):
          print(x , a-x,)
          break
      


# def is_prime(n):
#     if n == 1:
#         return False
#     for j in range(2, int(n**0.5) + 1):
#         if n % j == 0:
#             return False
#     return True