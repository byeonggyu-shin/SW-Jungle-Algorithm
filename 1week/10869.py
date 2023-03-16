# 문제
# 두 자연수 A와 B가 주어진다. 이때, a+b, a-b, a*b, a/b(몫), a%b(나머지)를 출력하는 프로그램을 작성하시오. 

# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ a, b ≤ 10,000)

# 출력
# 첫째 줄에 a+b, 둘째 줄에 a-b, 셋째 줄에 a*b, 넷째 줄에 a/b, 다섯째 줄에 a%B를 출력한다.
a,b = [int(x) for x in input().split()]

# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)

print(a + b, a - b, a * b, a // b, a % b)