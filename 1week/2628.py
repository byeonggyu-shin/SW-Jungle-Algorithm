import sys 

x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

cuts = []
for _ in range(n):
    direction, cut = map(int, sys.stdin.readline().split())
    cuts.append((direction, cut))

cuts.sort(key=lambda x: x[1], reverse=True)

max_width = x
max_height = y

for direction, cut in cuts:
    if direction == 0:
        max_height = max(max_height, cut, y - cut)
    else:
        max_width = max(max_width, cut, x - cut)

print(max_width * max_height)

# import sys 

# x, y = map(int, sys.stdin.readline().split())
# if not (1 <= x <= 100 and 1 <= y <= 100):
#     sys.exit("Error: Invalid input for x and y.")
# n = int(sys.stdin.readline())
# if not (0 <= n <= 100):
#     sys.exit("Error: Invalid input for n.")

# cutting_points_x = [] 
# cutting_points_y = [] 
# for _ in range(n):
#     direction, cut = map(int, sys.stdin.readline().split())

#     if direction == 0:
#         cutting_points_y.append(cut)
#     if direction == 1:
#         cutting_points_x.append(cut)

# cutting_points_x.sort(reverse=True)
# cutting_points_y.sort(reverse=True)

# if not cutting_points_x:
#     cutting_points_x.append(x)
# if not cutting_points_y:
#     cutting_points_y.append(y)

# cuttedX = [x - cutting_points_x[0]]
# cuttedY = [y - cutting_points_y[0]]

# for i in range(len(cutting_points_x)-1):
#     cuttedX.append(cuttedX[i]-cutting_points_x[i+1])

# for i in range(len(cutting_points_y)-1):
#     cuttedY.append(cuttedY[i]-cutting_points_y[i+1])

# x_length = max(cuttedX)
# y_length = max(cuttedY)

# print(x_length * y_length)

#   def cutting(i,c):
#     if i-c >= c:
#       i = i-c
#     else:
#       i = c
#     return i
  
#   if dir == 0:
#     if cut >=bigY: 
#       bigY =cut
#       y = cutting(y,cut)
#   if dir == 1:
    
#     if cut >= bigX: 
#       bigX =cut
#       x = cutting(x,cut)
# print(x*y)

