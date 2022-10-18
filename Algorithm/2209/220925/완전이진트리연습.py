# 완전이진트리 노드는 왼쪽 자식부터 채워진다

def inorder(n):
    if n <= V:
        inorder(2*n)
        tree.append(n)
        inorder(2*n+1)

V = int(input())
E = V + 1
tree = [0]  # 트리의 값은 노드의 번호, 트리의 인덱스는 노드의 값
inorder(1)

print(tree)
