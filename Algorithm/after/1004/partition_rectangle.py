N = 4
arr = [[0] * N for _ in range(N)]

def set_rect(r1, c1, r2, c2, val):
    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = val

for i in range(1, N-1+1):
    for j in range(1, N-1+1):
        # (0,0) -> (i-1,j-1)
        set_rect(0, 0, i, j, 1)
        # (0, j) -> (i-1, N-1)
        set_rect(0, j, i, N, 2)
        # (i, 0) -> (N-1, j-1)
        set_rect(i, 0, N, j, 3)
        # (i, j) -> (N-1, N-1)
        set_rect(i, j, N, N, 4)

        for line in arr:
            print(*line)
        print('---------------')