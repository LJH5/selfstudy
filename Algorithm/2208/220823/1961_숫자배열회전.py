# 90도 회전
def rotate_90(arr):
    rotated_matrix = [[0] * n for _ in range(n)]  # 초기화

    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - i - 1] = arr[i][j]
    return rotated_matrix

T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    matrix = [list(input().split()) for _ in range(n)]

    a = rotate_90(matrix)
    b = rotate_90(a)
    c = rotate_90(b)

    print(f'#{tc}')
    for i in range(n):
        print(''.join(a[i]), end= ' ')
        print(''.join(b[i]), end= ' ')
        print(''.join(c[i]), end= ' ')
        print()
