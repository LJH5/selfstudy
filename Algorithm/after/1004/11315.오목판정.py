import sys; sys.stdin = open('11315.txt')
dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]

def check_omok():
    global ans
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                continue
            # r, c : 모든 돌의 위치
            # (r, c)를 포함해서 5칸 연속으로 돌이 있는지는 체크
            for i in range(4):      # 방향
                for j in range(1, 5):  # 4칸 전진
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    # 범위 체크
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    if arr[nr][nc] == '.':
                        break
                else:
                    # 오목 완성
                    ans = 'YES'
                    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = 'NO'
    check_omok()
    print(f'#{tc} {ans}')
