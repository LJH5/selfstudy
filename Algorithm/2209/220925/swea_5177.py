# 이진힙
# 완전 이진 트리
# 부모노드 < 자식노드
# 부모노드 > 자식노드면 자리 바꾸기
# 부모 노드의 번호 = int(자식 노드의 번호/2)

def heap(n):
    if tree[int(n/2)] > tree[n]:
        tree[int(n/2)], tree[n] = tree[n], tree[int(n/2)]
        heap(int(n/2))

T = int(input())
for tc in range(1, T+1):
    result = 0
    V = int(input())
    tree = [0] + list(map(int, input().split()))

    for i in range(2, V+1):
        heap(i)

    while V:
        V = int(V/2)
        result += tree[V]
    print(f'#{tc} {result}')