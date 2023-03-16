import sys

n = int(sys.stdin.readline())

for i in range(n):
    test = sys.stdin.readline().strip() 
    score = 0
    combo = 0 
    for j in test:
        if j == 'O':
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)