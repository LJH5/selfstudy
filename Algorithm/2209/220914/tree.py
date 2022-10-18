'''
정점 번호: V = 1~(E+1)
간선 수: E = 4
부모-자식 순: 1 2 1 3 3 4 3 5
(1-2, 1-3, 3-4, 3-5)
'''

# root 찾기
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없음, root
            return i
# 전위 순회
def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

# 중위 순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])

# 후위 순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n,end=' ')

E = int(input())
arr = list(map(int, input().split()))
V = E + 1

ch1 = [0]*(V + 1)
ch2 = [0]*(V + 1)
# 방법2
# for i in range(0, E*2, 2):
#     p, c = arr[i], arr[i+1]
par = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

root = find_root(V)

preorder(root)