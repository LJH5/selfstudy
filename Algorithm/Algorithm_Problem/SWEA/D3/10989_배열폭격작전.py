# N: 지도의 크기, M: 폭탄의 수
# 지도는 적군의 수를 배열로 표시
# 폭탄 투하 좌표와 폭발력
# 폭발의 범위는 상하좌우로 * 폭발력

def bomb(r, c, p):     # 폭발로 적이 죽는 좌표를 저장하는 함수
    global kill_point
    kill_point.add((r, c))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    for k in range(4):
        for i in range(1, p+1):
            nr = r + dr[k]*i
            nc = c + dc[k]*i
            if 0 <= nr < N and 0 <= nc < N:
                kill_point.add((nr, nc))

def sum_kill(kill_data):     # 좌표의 적군의 수 총합을 반환하는 함수
    total_sum = 0
    for y, x in kill_data:
        total_sum += enemy_map[y][x]
    return total_sum

for tc in range(int(input())):
    N, M = map(int, input().split())
    enemy_map = [list(map(int, input().split())) for _ in range(N)]
    kill_point = set()
    for i in range(M):
        r_point, c_point, power = map(int, input().split())
        bomb(r_point, c_point, power)

    result = sum_kill(kill_point)

    print(f'#{tc+1} {result}')