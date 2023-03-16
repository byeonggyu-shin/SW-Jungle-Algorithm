import sys
lst = []
  
for _ in range(9):
    lst.append(int(sys.stdin.readline()))

for i in lst:
    lst2 = lst.copy()
    lst2.remove(i)
    for j in lst2:
        lst3 = lst2.copy()
        lst3.remove(j)
        if sum(lst3) == 100:
          for i in sorted(lst3):
            print(i)
          exit()


# 완전탐색
# import itertools

# lst = []
  
# for _ in range(9):
#     lst.append(int(sys.stdin.readline()))

# combs = itertools.combinations(lst, 7)  # 9개 숫자 중 7개 뽑기

# for comb in combs:
#     if sum(comb) == 100:  # 합이 100인 경우
#         print(sorted(comb))


# 백트래킹
# import sys

# def backtrack(total, cnt, idx):
#     if total == 100 and cnt == 7:  # 합이 100이 되고, 7개의 숫자를 뽑은 경우
#         for num in selected:
#             print(num)
#         sys.exit(0)  # 첫 번째 경우만 출력하고 종료
#         return
#     if total > 100 or cnt > 7 or idx == len(nums):  # 불가능한 경우
#         return
    
#     selected.append(nums[idx])  # 현재 숫자를 선택하고 다음 탐색
#     backtrack(total+nums[idx], cnt+1, idx+1)
#     selected.pop()  # 현재 숫자를 선택하지 않고 다음 탐색
#     backtrack(total, cnt, idx+1)

# # 입력 받기
# n = 9
# nums = []
# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))

# # 백트래킹 알고리즘 실행
# selected = []
# backtrack(0, 0, 0)