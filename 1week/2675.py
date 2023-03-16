n = int(input())

for i in range(n):
    r, s = input().split()
    result = ''
    for j in s:
        result += j * int(r)
    print(result)