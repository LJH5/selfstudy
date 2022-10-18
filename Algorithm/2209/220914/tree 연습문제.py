'''
정점 번호: V = 13
간선 수: E = V - 1 = 12
부모-자식 순: 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

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
        print(n, end=' ')

V = int(input())
arr = list(map(int, input().split()))
E = V - 1

ch1 = [0]*(V + 1)   # 왼쪽 자식
ch2 = [0]*(V + 1)   # 오른쪽 자식

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:     # 일단 왼쪽 자식부터 채우고
        ch1[p] = c
    else:
        ch2[p] = c      # 왼쪽 자식이 있으면 오른쪽 자식 채운다

preorder(1)

