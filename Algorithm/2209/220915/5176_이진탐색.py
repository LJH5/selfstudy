# 완전 이진트리, 중위 순회
# 루트노트의 값과, N/2 번 노드의 값을 출력
def inorder(n):
    global result
    if n <= N:
        inorder(2*n)                    # 중위 순회 하면서 노드의 번호 순서대로
        tree.append(n)                  # tree에 저장함
        inorder(2*n+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    E = N - 1
    tree = [0]                           # tree의 값은 노드 번호, index는 노드 값
    inorder(1)
    root = tree.index(1)                 # root의 노드 번호는 1번, 값이 1인 것의 인덱스
    ans = tree.index(int(N/2))           # 노드의 번호가 N/2인 것의 값은 인덱스

    print(f'#{tc} {root} {ans}')