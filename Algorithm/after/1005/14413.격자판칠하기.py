import sys; sys.stdin = open('14413.txt')

def check_arr(even, odd):
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '?': continue
            if (r + c) % 2:
                if arr[r][c] != odd:
                    return False
            else:
                if arr[r][c] != even:
                    return False
    return True

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ret1 = check_arr('#', '.')
    ret2 = check_arr('.', '#')

    ans = 'impossible'
    if ret1 or ret2:
        ans = 'possible'
    print(f'#{tc} {ans}')
