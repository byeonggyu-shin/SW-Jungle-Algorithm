import sys

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left_lst = merge_sort(lst[:mid])
    right_lst = merge_sort(lst[mid:])
    
    return merge(left_lst, right_lst)

def merge(left_lst, right_lst):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left_lst) and right_idx < len(right_lst):
        if left_lst[left_idx] < right_lst[right_idx]:
            result.append(left_lst[left_idx])
            left_idx += 1
        else:
            result.append(right_lst[right_idx])
            right_idx += 1
    
    if left_idx < len(left_lst):
        result.extend(left_lst[left_idx:])
    if right_idx < len(right_lst):
        result.extend(right_lst[right_idx:])
    
    return result

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

sorted_lst = merge_sort(lst)
for num in sorted_lst:
    print(num)