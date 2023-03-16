import sys

n = int(sys.stdin.readline())
lst = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(1, 10001):
    for j in range(lst[i]):
        sys.stdout.write(str(i) + '\n')
# import sys

# def counting_sort(lst):
#     # 입력 리스트의 최대값을 찾습니다. 
#     max_val = max(lst)

#     # 각 값이 나타나는 횟수를 저장하는 리스트를 생성합니다.
#     count_lst = [0] * (max_val + 1)

#     # 각 값이 나타나는 횟수를 세어서 count_lst에 저장합니다.
#     for val in lst:
#         count_lst[val] += 1

#     # count_lst의 누적합을 계산합니다.
#     for i in range(1, max_val + 1):
#         count_lst[i] += count_lst[i - 1]

#     # lst를 역순으로 순회하면서 정렬된 리스트를 생성합니다.
#     sorted_lst = [0] * len(lst)
#     for val in reversed(lst):
#         idx = count_lst[val] - 1
#         sorted_lst[idx] = val
#         count_lst[val] -= 1

#     return sorted_lst

# n = int(sys.stdin.readline())
# lst = []
# for _ in range(n):
#     lst.append(int(sys.stdin.readline()))

# for num in counting_sort(lst):
#     sys.stdin.readline(str(num) + '/n')