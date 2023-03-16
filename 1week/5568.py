# from itertools import permutations

# n = int(input())
# k = int(input())
# cards = [input() for _ in range(n)]

# # k개의 카드를 선택한 후, 이를 나열하는 모든 경우를 구한다.
# perms = permutations(cards, k)
# result = set()
# for perm in perms:
#     num = ''.join(perm)
#     result.add(num)
# # 중복을 제거한 결과의 개수를 출력한다.
# print(len(result))


def card_pick(k, picked, cards, result):
    if len(picked) == k: # k개의 카드를 뽑았을 때
        num = ''.join(picked)
        result.add(num)
        return
    for i in range(len(cards)):
        card = cards[i]
        card_pick(k, picked + [card], cards[:i] + cards[i+1:], result) # 뽑은 카드를 picked에 추가하고, 뽑은 카드를 제외한 나머지 카드들로 재귀 호출

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
result = set()
card_pick(k, [], cards, result)
print(len(result))