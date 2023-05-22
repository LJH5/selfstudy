import sys
input = sys.stdin.readline


def preorder(n):
    if n > 0:
        print(chr(n + 64), end='')
        preorder(lc[n])
        preorder(rc[n])


def inorder(n):
    if n > 0:
        inorder(lc[n])
        print(chr(n + 64), end='')
        inorder(rc[n])


def postorder(n):
    if n > 0:
        postorder(lc[n])
        postorder(rc[n])
        print(chr(n + 64), end='')


V = int(input())

lc = [0] * (V + 1)
rc = [0] * (V + 1)

for i in range(1, V + 1):
    p, l, r = input().split()
    lc[ord(p) - 64] = ord(l) - 64   # 알파벳을 아스키 코드로 숫자로 바꿔서 처리
    rc[ord(p) - 64] = ord(r) - 64

# print(lc)
# print(rc)

preorder(1)
print()
inorder(1)
print()
postorder(1)
