# 대각선 달팽이로 풀어보자!
def snail(r, c, cycle):
    if cycle == 0:                  # 모든 사이클을 실행 했으면 
        return                      # 함수 종료
    # print('-----', N // 2 + 1 - cycle + 1, '사이클-----')
    dr = [1, 1, -1, -1]             # 회전하는 방향은 우하, 좌하, 좌상, 우상
    dc = [1, -1, -1, 1]
    nr, nc = 0, 0                   # 재귀를 사용하니까 변수 생성 및 초기화
    for k in range(4):              # 4방 탐색
        # print('r:', r, 'c:', c)
        for i in range(cycle):      # 범위 안에서 돌도록 컨트록
            nr = r + dr[k]*i        # 다음 r 좌표
            nc = c + dc[k]*i        # 다음 c 좌표
            # print('nr:', nr, 'nc:', nc)
            visited.add((nr, nc))   # 방문한 곳으로 저장, set이니까 중복 생각 없이 저장
        r, c = nr, nc               # 한 변 이동하면 시작점 갱신
    snail(r+1, c, cycle-1)          # 다음 사이클로 이동

def sum_snail(arr):
    total_sum = 0                   # 농작물의 총합을 저장할 변수
    for r, c in arr:                # visited에 저장된 튜플을 하나씩 가져옴
        total_sum += farm[r][c]     # 해당 좌표의 농작물 수를 더해줌
    return total_sum                # 총합을 반환

for tc in range(int(input())):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    visited = set()                     # 방문한 곳을 저장
    snail(0, N//2, N//2 + 1)            # 시작 지점의 r좌표와 c좌표, 회전하는 수
    result = sum_snail(visited)         # 반환된 농작물의 총합을 저장
    print(f'#{tc+1} {result}')