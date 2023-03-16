import sys
import itertools

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

lst.sort()

cases = itertools.permutations(lst)  


max = 0

for case in cases:
    sum = 0
    for i in range(len(case)-1):
      sum += abs(case[i] - case[i+1])
      if sum > max:
          max = sum

print(max)



#  리스트 idx 0 , 

#  양수 이면서 가장 작은수 0번 절댓값이 가장 작은수
#  가장 큰 음수 마지막 idx or 가장 작은 양수

#  10-4 4-20 20-1 1-15 15-8  
#   6    16    19  14   7

#  4  2   6  1  5  3