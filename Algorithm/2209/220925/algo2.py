# 이진트리
def preorder(n):
    if n < V+1:
        pre_tree.append(n)
        preorder(2*n)
        preorder(2*n+1)

def inorder(n):
    if n < V+1:
        inorder(2*n)
        in_tree.append(n)
        inorder(2*n+1)

def postorder(n):
    if n < V+1:
        postorder(2*n)
        postorder(2*n+1)
        post_tree.append(n)

T = int(input())
for tc in range(1, T+1):
    V = int(input())
    pre_tree = [0]              # 전위순회 저장
    in_tree = [0]               # 중위순회 저장
    post_tree = [0]             # 후위순회 저장
    tree = [0]                  # T2 트리를 저장
    result = [0]*V              # T2 트리를 전위순회한 결과를 저장

    preorder(1)
    inorder(1)
    postorder(1)

    for i in range(1, V+1):
        tree.append(max(pre_tree[i], in_tree[i], post_tree[i]))

    for j in range(1, len(in_tree)):
        result[in_tree[j] - 1] = tree[j]

    print(f'#{tc}', end=' ')
    print(*result)