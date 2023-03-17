# 그래프 탐색 기본 (하) - 이진 검색 트리

import sys
sys.setrecursionlimit(10**6)  

# 루트 부터 왼쪽으로 차례대로 노드에 넣고
# 출력은 후위 순회한 결과 출력 

class Node:
  def __init__(self, value):
    self.item = value
    self.left = None
    self.right = None

def insert_node(node, value):
    if node is None:
        return Node(value)
    else:
        if value < node.value:
            node.left = insert_node(node.left, value)
        else:
            node.right = insert_node(node.right, value)
    return node

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.item)
  
root = None

while True:
    try:
        value = int(sys.stdin.readline())
    except:  # 입력이 끝나면 종료합니다.
        break

    if not root:
        root = Node(value)
    else:
        insert_node(root, value)

