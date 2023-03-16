
#  재귀
import sys

t = int(sys.stdin.readline())

lst = []
for _ in range(t):
    lst.append(int(sys.stdin.readline()))

def findCase (n):
    if n == 0:
        return  [[]]

    result = []
    # result = 0
    for i in [1, 2, 3]:
        if n - i >= 0:
            for j in findCase (n - i):
                result.append([i] + j)
                # result += 1

    return result

for i in lst:
    print(len(findCase(i)))
    # print(findCase(i))
  
# 도수 정렬

# arr = [0] * 11
# arr[1] = 1
# arr[2] = 2
# arr[3] = 4

# n =int(input())
# while n>0:
#     c =int(input())
#     for i in range(4,c+1):
#         arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
#     print(arr[c])
#     n -= 1

