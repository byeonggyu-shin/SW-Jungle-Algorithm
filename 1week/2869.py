# import sys
# a,b,v = map(int, sys.stdin.readline().split())

# dst = 0
# time = 1
# while dst < v:
#   dst += a
#   if dst >= v:
#     break
#   if dst < v:
#     dst -= b
#     time += 1
# print(time)
    
import sys

a, b, v = map(int, sys.stdin.readline().split())

dst = a - b
days, remainder = divmod(v - a, dst)

if remainder == 0:
    print(days + 1)
else:
    print(days + 2)

# import sys

# a, b, v = map(int, sys.stdin.readline().split())

# climbed_height = 0
# time = 0
# while climbed_height <= v - a:
#     climbed_height += a - b
#     time += 1

# print(time + 1)