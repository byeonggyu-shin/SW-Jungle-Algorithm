# 스택 (상) - 히스토그램에서 가장 큰 직사각형

import sys

while True:
    heights = list(map(int, sys.stdin.readline().split()))
    if heights[0] == 0:
        break

    heights.pop(0)
    heights.append(0)
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    print(max_area)