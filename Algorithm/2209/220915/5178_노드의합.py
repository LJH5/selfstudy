# N: 노드의 개수, M: 리프 노드의 개수, L: 값을 출력할 노드의 번호
# L 노드의 자식들 중 리프 노드의 값을 모두 더하면 된다
def sum(n):
    global result
    if n <= V:
        result += tree[n]
        sum(2 * n)
        sum(2 * n + 1)

T = int(input())
for tc in range(1, T+1):
    V, M, L = map(int, input().split())
    tree = [0]*(V+1)
    result = 0
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    # L의 자식들을 모두 더한다
    sum(L)
    print(f'#{tc} {result}')

