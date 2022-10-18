def preorder(n):
    if n <= size:
        print(tree[n], end=' ')
        preorder(2*n)
        preorder(2*n+1)


def inorder(n):
    if n <= size:
        preorder(2*n)
        print(tree[n], end=' ')
        preorder(2*n+1)


tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']
size = len(tree) - 1

preorder(1)
print()
inorder(1)