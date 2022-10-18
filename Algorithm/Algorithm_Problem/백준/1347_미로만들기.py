# 내용의 길이는 50이하
# 미로의 최대 크기는 50 * 50
# 시작 좌표는 랜덤
# 남쪽을 바라보고 시작
# 정사각형은 한 점과 한 변의 길이만 알면 됨
maze = [['#']*101 for _ in range(101)]
N = int(input())
text = input()
# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
visited = set()             # 방문한 곳 찍기
d = 0                       # 처음 방향은 남쪽
r, c = 50, 50               # 미로의 가운데서 시작
visited.add((r, c))         # 시작점 방문 확인
maze[r][c] = '.'            # 시작점에 '.' 찍기
for i in text:              # 문자 다 쓸때까지 가져오기
    if i == 'F':            # 전진이면
        r += dr[d]          # 해당 방향으로 전진
        c += dc[d]          # 해당 방향으로 전진
        maze[r][c] = '.'    # 서있는 곳 '.' 찍기
        visited.add((r, c)) # 방문 확인
    elif i == 'R':          # R이면
        d = (d + 1) % 4     # 오른쪽으로 돌기
    else:                   # L이면
        d = (d + 3) % 4     # 왼쪽으로 돌기
                            # 모든 문자 사용함
max_r, max_c = 0, 0         # 최대값 생성
min_r, min_c = 100, 100     # 최소값 생성
for i in visited:           # 방문한 곳을 가져옴
    if max_r < i[0]:        # '.'이 가장 오른쪽에 있는 위치 찾기
        max_r = i[0]
    if min_r > i[0]:        # '.'이 가장 왼쪽에 있는 위치 찾기
        min_r = i[0]
    if max_c < i[1]:        # '.'이 가장 위쪽에 있는 위치 찾기
        max_c = i[1]
    if min_c > i[1]:        # '.'이 가장 아래쪽에 있는 위치 찾기
        min_c = i[1]

for i in range(min_r, max_r+1):
    print(''.join(maze[i][min_c: max_c+1]))