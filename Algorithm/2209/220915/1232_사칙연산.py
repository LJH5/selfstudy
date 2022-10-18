for tc in range(1, 11):
    V = int(input())
    lc = [0] * (V + 1)
    rc = [0] * (V + 1)
    tree = [0] * (V + 1)

    for i in range(1, V+1):
        data = list(input().split())
        if len(data) == 4:
            tree[i] = data[1]
            lc[i] = int(data[2])
            rc[i] = int(data[3])
        else:
            tree[i] = int(data[1])

    oper = {'+', '-', '*', '/'}
    for n in range(len(tree)-1, 0, -1):                         # 나중에 들어온 연산자 부터 계산해야 순서가 맞음
        if tree[n] in oper:                                     # 부모가 연산자이면
            if tree[n] == '+':                                  # 자식을 해당 연산자에 맞게 처리
                tree[n] = tree[lc[n]] + tree[rc[n]]
            elif tree[n] == '-':
                tree[n] = tree[lc[n]] - tree[rc[n]]
            elif tree[n] == '/':
                tree[n] = int(tree[lc[n]] / tree[rc[n]])
            else:
                tree[n] = tree[lc[n]] * tree[rc[n]]
    print(f'#{tc} {tree[1]}')
