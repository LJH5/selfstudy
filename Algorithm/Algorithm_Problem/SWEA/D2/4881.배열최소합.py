def perm(depth):
    global result, tmp
    if tmp >= result:
        return
    if depth == n:
        if tmp < result:
            result = tmp
        return
    for i in range(n):
        if not check[i]:
            check[i] = 1
            tmp += matrix[depth][i]     # 임시 합에 더하면서
            perm(depth+1)               # 재귀로 들어가기
            tmp -= matrix[depth][i]     # return으로 빠져나오면 빼주기
            check[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    check = [0]*n
    result = 999    # 최소 합을 저장할 변수
    tmp = 0         # 임시로 합을 저장할 변수

    perm(0)

    print(f'#{tc} {result}')