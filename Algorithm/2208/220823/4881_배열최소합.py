T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(matrix)
    print(f'#{tc} {result}')