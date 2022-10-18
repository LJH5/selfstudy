from collections import deque
# 상하좌우
# 0은 빈공간, 1은 장애물, 2는 방어탑
# 방어탑에서 사방탐색을 해서 1이면 막히고 아니면 직선으로 쭉 나감
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    tw_idx = []
    result = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == 2:
                tw_idx.append((i, j))
            elif field[i][j] == 0:
                result += 1
    visited = set()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    q = deque()
    attack = 0
    # 타워에 저장되어 있는 좌표를 하나씩 가져옴
    for r, c in tw_idx:
        # 방문한 곳이 아니라면 저장
        if (r, c) not in visited:
            visited.add((r, c))
            q.append((r, c))
            tmp = 0
            while q:
                y, x = q.popleft()
                # 사방 탐색
                for k in range(4):
                    # 방어탑의 공격은 일직선으로 쭉 날아감
                    for i in range(1, N):
                        ny = y + dr[k]*i
                        nx = x + dc[k]*i
                        # 범위를 벗어나면 쳐내기
                        if ny < 0 or ny >= N or nx < 0 or nx >= N:
                            break
                        # 공격이 막히면 쳐내기
                        if field[ny][nx] == 1 or field[ny][nx] == 2:
                            break
                        # 공격 범위면
                        if field[ny][nx] == 0 and (ny, nx) not in visited:
                            attack += 1
                            visited.add((ny, nx))
    result -= attack
    print(f'#{tc} {result}')