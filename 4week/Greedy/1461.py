# 그리디 - 도서관

import sys

n, m = map(int, sys.stdin.readline().split())
books = sorted(list(map(int, sys.stdin.readline().split())))
# 양수 음수 두 개의 목록으로 분리 , 절대값의 내림차순으로 정렬
l_books = sorted([-x for x in books if x < 0], reverse=True)
r_books = sorted([x for x in books if x > 0], reverse=True)
# 걸어야 하는 거리를 계산 앞뒤로 가야 하니 x2
l_dist = [2 * l_books[i] for i in range(0, len(l_books), m)]
r_dist = [2 * r_books[i] for i in range(0, len(r_books), m)]
# 양쪽의 거리 합 => 총 거리 
total_distance = sum(l_dist) + sum(r_dist)

if l_books and r_books:
    book = max(l_books[0], r_books[0])
else:
    book = l_books[0] if l_books else r_books[0]
# 돌아갈 필요가 없으니 제일 긴 거리를 뺌
result = total_distance - book
print(result)
