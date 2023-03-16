import sys

n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(lst)

while left <= right:
    mid = (left + right) // 2

    #  lst에서 mid일때 잘라지는 부분
    #  만약 el > mid 면 el - mid 아니면 0 
    # 을  lst 에서 반복하는 요소 el 에 적용한다
    # result = []
    # for el in lst:
    #     if el > mid:
    #         result.apped(el - mid)
    #     else:
    #         result.append(0)
    # total = sum(result)
                  

    total = sum( el - mid if  el > mid else 0 for  el in lst)
    if total > m:
        left = mid + 1
      
    elif total == m:
        print(mid)
        sys.exit()
    else:
        right = mid - 1
    

print(right)


#  lst 의 모든 el 에 -h 후 남은 값을 sum = m 이 나와야한다.
#  큰수부터?
#  중간 값이 무엇일까

