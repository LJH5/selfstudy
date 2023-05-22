import sys
sys.stdin = open('input.txt')


def find_tank():                                        # 탱크의 위치와 방향을 찾는 함수
    for i in range(N):                                  # 배열의 모든 좌표를
        for j in range(M):                              # 탐색하여서
            if field[i][j] in tank_icon:                # 탱크의 아이콘이면
                d = tank_icon.index(field[i][j])        # 탱크의 방향을 저장하고
                return i, j, d                          # 좌표와 방향을 반환


def shoot(info):                                        # 발사할 때를 처리할 함수
    r, c, d = info                                      # 좌표와 탱크의 방향
    nr = r + dr[d]                                      # 발사 시 날아가는 좌표
    nc = c + dc[d]                                      # 발사 시 날아가는 좌표
    if nr < 0 or nr >= N or nc < 0 or nc >= M:          # 범위를 벗어나면
        return                                          # 함수 종료
    if field[nr][nc] == '*':                            # 벽돌 벽이면
        field[nr][nc] = '.'                             # 부셔버리기
        return                                          # 함수 종료
    elif field[nr][nc] == '.' or field[nr][nc] == '-':  # 평지나 물일 경우
        shoot((nr, nc, d))                              # 포탄은 계속 날아간다 다음 좌표를 갱신, 방향은 유지
    else:                                               # 강철벽이라 안 부서지는 경우
        return                                          # 함수 종료


def move_tank(r, c, d):                                 # 탱크 이동 시 배열을 갱신하는 함수
    global tank_info                                    # 탱크의 좌표와 방향이 저장되어있는 변수
    field[r][c] = tank_icon[d]                          # 탱크의 방향을 회전
    tank_info = (r, c, d)                               # 배열에서 탱크의 아이콘을 d 방향으로 갱신
    nr = r + dr[d]                                      # d 방향으로 이동 시 새로운 이동 좌표
    nc = c + dc[d]                                      # d 방향으로 이동 시 새로운 이동 좌표
    if nr < 0 or nr >= N or nc < 0 or nc >= M:          # 이동 좌표가 범위를 벗어나면
        return                                          # 함수 종료
    if field[nr][nc] == '.':                            # 이동 좌표가 평지라면
        field[r][c] = '.'                               # 배열의 탱크 위치는 평지로 갱신
        field[nr][nc] = tank_icon[d]                    # 이동한 좌표에 d 방향 탱크 아아콘을 넣어줌
        tank_info = (nr, nc, d)                         # 탱크의 좌표와 방향을 갱신


def play_game():
    for command in command_list:                        # 커멘드 하나씩 입력하기
        if command == 'S':                              # 발사이면
            shoot(tank_info)                            # 탱크의 좌표와 방향 정보 보내기
        elif command == 'U':                            # 위쪽으로 이동이면
            move_tank(tank_info[0], tank_info[1], 0)    # 탱크의 현재 위치와 위쪽 방향
        elif command == 'R':                            # 오른쪽으로 이동이면
            move_tank(tank_info[0], tank_info[1], 1)    # 탱크의 현재 위치와 오른쪽 방향
        elif command == 'D':                            # 아래쪽으로 이동이면
            move_tank(tank_info[0], tank_info[1], 2)    # 탱크의 현재 위치와 아래쪽 방향
        else:                                           # 왼쪽으로 이동이면
            move_tank(tank_info[0], tank_info[1], 3)    # 탱크의 현재 위치와 왼쪽 방향


for tc in range(int(input())):
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    command_cnt = int(input())
    command_list = list(input())

    tank_icon = ['^', '>', 'v', '<']                    # 위쪽, 오른쪽, 아래쪽, 왼쪽
    dr = [-1, 0, 1, 0]                                  # 탱크 아이콘과 인덱스 맞추기
    dc = [0, 1, 0, -1]                                  # 상우하좌
    tank_info = find_tank()                             # 탱크의 좌표와 방향
    play_game()                                         # 게임 시작

    print(f'#{tc+1}', end=' ')
    for i in field:
        print(''.join(i))
