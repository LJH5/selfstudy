def preorder(n):
    if n:
        print(n, end=' ')
        preorder(lc[n])
        preorder(rc[n])

def inorder(n):
    if n:
        inorder(lc[n])
        print(n, end=' ')
        inorder(rc[n])

def postorder(n):
    if n:
        postorder(lc[n])
        postorder(rc[n])
        print(n, end=' ')


V, E = map(int,input().split())
tree = list(map(int, input().split()))
lc = [0]*(V+1)
rc = [0]*(V+1)

for i in range(E):
    p, c = tree[2*i], tree[2*i+1]
    if lc[p] == 0:
        lc[p] = c
    else:
        rc[p] = c
print('전위 순회 : ', end=' ')
preorder(1)
print()
print('중위 순회 : ', end=' ')
inorder(1)
print()
print('후위 순회 : ', end=' ')
postorder(1)