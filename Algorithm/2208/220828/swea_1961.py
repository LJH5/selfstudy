def rotate(arr):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-1-i] = arr[i][j]
    return tmp
T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    matrix = [list(input().split()) for _ in range(n)]

    a = rotate(matrix)
    b = rotate(a)
    c = rotate(b)

    print(f'#{tc}')
    for i in range(n):
        print(''.join(a[i]), end=' ')
        print(''.join(b[i]), end=' ')
        print(''.join(c[i]), end=' ')
        print()
