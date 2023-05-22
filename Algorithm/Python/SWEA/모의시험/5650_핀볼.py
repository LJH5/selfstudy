# -1: 블랙홀, 만나면 게임 종료
# 1: 아래쪽 -> 오른쪽, 오른쪽 -> 위쪽, 나머지 반대
# 2: 위쪽 -> 오른쪽, 왼쪽 -> 아래쪽, 나머지 반대
# 3: 위쪽 -> 왼쪽, 왼쪽 -> 아래쪽, 나머지 반대
# 4: 아래쪽 -> 왼쪽, 오른쪽 -> 위쪽, 나머지 반대
# 5: 다 반대
# 6 ~ 10: 웜홀, 해당하는 번호가 2개 있으면서 웜홀에 들어가면 같은 번호의 다른 웜홀로 나온다
# 핀볼은 상하좌우
# 핀볼이 1 ~ 4번 블록에 부딪칠때마다 +1점
# 핀볼이 블랙홀로 들어가거나 시작점으로 돌아오면 게임 종료
# 무작위 위치에서 시작할 때 최고 점수를 구하여라
# 모든 점에서 사방탐색을 시작한다?
def find_start_point():
    global start_r, start_c
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:                        # 출발점을 찾으면
                start_r = i
                start_c = j
                for direction in range(4):              # 특정한 방향을 가지고
                    go(i, j, direction, 0)              # 게임 시작


def go(r, c, d, cnt):                                   # 한방향으로 쭉 날아감
    global result
    while True:
        nr = r + dr[d]
        nc = c + dc[d]
        if board[nr][nc] == -1 or (nr, nc) == (start_r, start_c):   # 블랙홀이거나 출발점으로 돌아오면
            if cnt > result:
                result = cnt
            break
        if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 벽을 만나면
            cnt += 1                                # 점수를 1점 올리고
            d = (d + 2) % 4                         # 방향을 반대로 바꾸고
            continue
        if 0 < board[nr][nc] < 6:                   # 블럭을 만나면
            cnt += 1                                # 점수를 1점 올리고
            d = change_direction(board[r][c], d)    # 블럭의 번호와 방향을 고려해 방향을 갱신하고
        elif 6 <= board[nr][nc]:                    # 웜홀을 만나면
            r, c = wormhole(board[nr][nc], nr, nc)  # 웜홀에서 빠져나온 위치


def change_direction(block_num, d):
    if (block_num == 1 and d == 2) or (block_num == 2 and d == 0):
        nd = 1
    elif (block_num == 1 and d == 3) or (block_num == 4 and d == 1):
        nd = 0
    elif (block_num == 2 and d == 3) or (block_num == 3 and d == 1):
        nd = 2
    elif (block_num == 3 and d == 0) or (block_num == 4 and d == 2):
        nd = 3
    else:
        nd = (d + 2) % 4
    return nd


def wormhole(wormhole_num, now_r, now_c):               # 웜홀을 처리하는 함수
    for i in range(N):                                  # 같은 번호의 웜홀을
        for j in range(N):                              # 찾아보자
            if board[i][j] == wormhole_num:             # 같은 번호의 웜홀이 있으면
                if i != now_r and j != now_c:           # 들어온 웜홀이 아니면
                    return i, j                         # 웜홀의 위치 반환


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0]  # 상우하좌
    dc = [0, 1, 0, -1]
    result = 0
    start_r = 0
    start_c = 0
    find_start_point()
    # print(board)
    print(f'#{tc+1} {result}')