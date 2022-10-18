def preorder(n):
    if n <= V:
        print(n, end=' ')
        preorder(2*n)
        preorder(2*n+1)


V = 5
E = V - 1
preorder(1)