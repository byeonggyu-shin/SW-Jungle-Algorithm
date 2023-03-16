# Moo 게임

import sys

n =int(sys.stdin.readline())

# 길이가 3 3+4 3+4+5 .... 일떄 n번째 str이 무엇인가
# (3) + (3+4) + (3+4+5) ...

def moo_game(n):
    
    # 
    if n == 0:
        return "moo"
    elif n == 1:
        return "moo"
    else:
        i = 0
        while n > (i + 2 + moo_game(i)):
            i += 1
        if n == i + 1:
            return "m"
        elif n <= i + 2 + moo_game(i) - moo_game(i-1):
            return "o"
        else:
            return moo_game(n - i - 2 - moo_game(i))
        
print(moo_game(n))
