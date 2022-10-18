# N: 점원의 수, B: 선반의 높이
# 점원들의 키를 합쳐서 선반 이상인 높이를 만들고
# 그 중에서 최소를 구하라
def dfs(tmp_sum, depth):
    global result

    if depth == N:
        return

    if tmp_sum >= B:
        if B - tmp_sum < result:
            result = B - tmp_sum
            return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            dfs(tmp_sum + member[i], depth + 1)
            check[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    member = list(map(int, input().split()))    # 점원들의 키
    result = 0
    check = [0] * N
    dfs(0, 0)
    print(f'#{tc}')
