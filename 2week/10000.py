import sys

n = int(sys.stdin.readline())
circles = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
circles.sort() 

stack = []
cnt = 1

for circle in circles:
    while stack and stack[-1][1] < circle[0] - circle[2]:
        stack.pop()
    if stack:
        cnt += 1
    stack.append (circle)

print(cnt) 