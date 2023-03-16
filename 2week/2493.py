# import sys

# n = int(sys.stdin.readline())
# lst = list(map(int,sys.stdin.readline().split()))

# result = []
# for i in range(n):
#   if i > 0:
#     for x , y in enumerate(lst[:i][::-1]):
#       if lst[i] <= y:
#         result.append(n-len(lst[i:]) -x)
#         break
#     else: 
#       result.append(0)
#   elif i == 0:
#     result.append(0)
# print(*result)


n = int(input())
heights = list(map(int, input().split()))
stack = []  # 탑의 정보를 저장할 스택
result = [0] * n  # 각 탑에서 보낸 신호를 수신하는 탑의 번호를 저장할 리스트

for i in range(n):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()  # 스택에서 높이가 낮은 탑 제거
    if stack:
        result[i] = stack[-1] + 1  # 스택의 맨 위 탑이 현재 탑에서 신호를 수신하는 탑
    stack.append(i)  # 현재 탑 정보 스택에 추가

print(*result)