# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# V: 노드의 수
# E: 간선의 수, V - 1
def preoder(n):             # 전위  순회
    if n:                   # 0번 노드가 아니면
        print(n, end=' ')   # 현위치 출력
        preoder(lc[n])      # 왼쪽 자식 노드로
        preoder(rc[n])      # 오른쪽 자식 노드로


def inoder(n):              # 중위 순회
    if n:                   # 0번 노드가 아니면
        inoder(lc[n])      # 왼쪽 자식 노드로
        print(n, end=' ')   # 현위치 출력
        inoder(rc[n])      # 오른쪽 자식 노드로


def postoder(n):            # 후위 순회
    if n:                   # 0번 노드가 아니면
        postoder(lc[n])      # 왼쪽 자식 노드로
        postoder(rc[n])      # 오른쪽 자식 노드로
        print(n, end=' ')   # 현위치 출력

V = int(input())
E = V - 1
tree = list(map(int, input().split()))
lc = [0] * (V + 1)                  # 0번 인덱스 제외, 인덱스는 노드의 번호
rc = [0] * (V + 1)
print(tree)
for i in range(E):
    p, c = tree[2*i], tree[2*i+1]   # 짝수 인덱스는 부모 노드, 홀수는 인덱스는 자식 노드
    if lc[p] == 0:
        lc[p] = c
    else:
        rc[p] = c

preoder(1)
print()
inoder(1)
print()
postoder(1)