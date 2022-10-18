# 이진 최소 힙, 완전 이진 트리
# 노드 추가 시 마지막 노드 뒤에 추가
# 부모 노드 값< 자식 노드 값, 노드 추가시 정렬
# 마지막 노드의 조상 노드 정수 합
# 마지막 노드의 조상 노드는 int(자식 노드 번호/2)
# root에 넣는다
# 부모와 자식을 비교한다
# 부모가 자식보다 크면 바꾼다
# 바꾼 것의 부모와 비교한다
def heap(i):
    if i < 1:
        return
    if tree[int(i / 2)] > tree[i]:
        tree[int(i / 2)], tree[i] = tree[i], tree[int(i / 2)]
        heap(int(i / 2))

T = int(input())
for tc in range(1, T+1):
    V = int(input())
    V_list = list(map(int, input().split()))
    tree = [0] + V_list
    result = 0
    #부모가 자식보다 크다면
    for i in range(2, len(tree)):
       heap(i)
    # 마지막 노드의 조상노드
    while V >= 1:
        V = int(V/2)
        result += tree[V]

    print(f'#{tc} {result}')
