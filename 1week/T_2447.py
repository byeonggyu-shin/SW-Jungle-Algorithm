import sys 

n = int(sys.stdin.readline())

def stars(n):
    if n == 1:
        return ['*']
    
    prev = stars(n // 3)
    result = []
    
    for i in range(3):
        for j in range(len(prev)):
            if i == 1:
                result.append(prev[j] + ' ' * (n // 3) + prev[j])
            else:
                result.append(prev[j] * 3)
    return result

print('\n'.join(stars(n)))

