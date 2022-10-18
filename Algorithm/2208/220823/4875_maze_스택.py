T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = set()
    result = 0
    print(f'#{tc} {result}')