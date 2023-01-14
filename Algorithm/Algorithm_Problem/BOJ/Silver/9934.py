def preorder(n):
    if n <= 2**depth - 1:
        preorder(2*n)
        tree.append(n)
        preorder(2*n+1)


depth = int(input())
tree = []
inorder_tree = list(map(int, input().split()))
preorder(1)
# print(tree)
# print(inorder_tree)
used = set()
for i in range(1, depth+1):
    for j in range(len(tree)):
        if tree[j] <= 2**i - 1 and tree[j] not in used:
            used.add(tree[j])
            print(inorder_tree[j], end=' ')
    print()