num1, num2 = input().split()

def reverse_str(s: str) -> str:
    return s[::-1]

reversed_num1 = reverse_str(num1)
reversed_num2 = reverse_str(num2)

if int(reversed_num1) > int(reversed_num2):
    print(reversed_num1)
else:
    print(reversed_num2)