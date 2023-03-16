# 문자열 폭발

import sys

string = sys.stdin.readline().rstrip()
bomb  = sys.stdin.readline().rstrip()

# 스택 ? 폭탄 찾는 함수 재귀?

# def findBomb(string ,bomb):

stack = []
len_bomb = len(bomb)

for i in string:
    stack.append(i)
    # 길면 체크 시작
    if len(stack) >= len_bomb:
        # 슬라이싱 해서 비교 슬라이싱이 문제인가? 
        if ''.join(stack[-len_bomb:]) == bomb:
            
            delBomb = 0
            while delBomb < len_bomb:
                stack.pop()
                delBomb += 1
            # stack = stack[:-len_bomb]


if len(stack):
    print(''.join(stack)) 
else: 
    print("FRULA")
            

# => 시간초과 문제가 뭘까? 


 