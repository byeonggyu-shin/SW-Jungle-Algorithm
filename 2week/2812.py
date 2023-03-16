import sys

n , k = map(int ,sys.stdin.readline().split())

nums = list(sys.stdin.readline())

stack = []

for num in nums:
    while k > 0 and stack and stack[-1] < num:
        stack.pop()
        k -= 1
    stack.append(num)

while k >0:
    stack.pop()
    k-= 1

print(''.join(stack))