# bfs로 풀기
# 한번 이동하면 비용은 1 증가
# 높은 곳으로 이동하면 비용은 높이 차이만큼 증가
# 비용을 저장할 테이블을 만들고
# 각 비용의 테이블을 다익스트라 처럼
# 비용이 최소이면 cost_arr에 저장하고 다음으로 이동
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_arr = [list(map(int, input().split())) for _ in range(N)]
    cost_arr = [[987654321]*N for _ in range(N)]                # 비용을 저장할 리스트
    cost_arr[0][0] = 0                                          # 시작점의 비용은 0
    q = deque()
    q.append((0, 0))                                            # 시작점을 넣어줌
    dr, dc = [-1, 1, 0, 0],  [0, 0, 1, -1]                      # 사방탐색의 재료
    
    while q:                                                    # q가 빌때까지 반복
        now = q.popleft()                                       # 갈 수 있는 위치를 뽑아옴
        r, c = now                                              # 현재 위치의 r, c 좌표
        for k in range(4):                                      # 사방탐색
            nr, nc = r + dr[k], c + dc[k]                       # 다음 위치 사방탐색
            if nr < 0 or nr >= N or nc < 0 or nc >= N:          # 범위를 벗어나면
                continue                                        # 반복문 다시 시작
            if map_arr[r][c] >= map_arr[nr][nc]:                # 다음 칸이 지금보다 작거나 같으면
                cost = 1                                        # 비용은 1
            else:                                               # 다음 칸이 지금보다 크면
                cost = 1 + map_arr[nr][nc] - map_arr[r][c]      # 비용은 1 +(높이차이)
            if cost_arr[nr][nc] > cost_arr[r][c] + cost:        # 다음 칸에 가는 비용이 지금+비용보다 작으면
                cost_arr[nr][nc] = cost_arr[r][c] + cost        # 비용을 더한뒤에
                q.append((nr, nc))                              # 다음 칸으로 이동

    result = cost_arr[N-1][N-1]                                 # 목적지에 저장된 최소 비용
    print(f'#{tc} {result}')

