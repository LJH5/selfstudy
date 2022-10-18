# N: 보드판 한 번의 길이, M: 돌을 놓는 횟수
# 좌표와 바둑돌의 색(1: 흑돌, 2: 백돌)
def setting():                                                        # 보드의 크기에 맞게 4개의 돌을 세팅하는 함수
    for i in range(2):
        for j in range(2):
            if i == j:
                board[N // 2 - i][N // 2 - j] = 2
            else:
                board[N // 2 - i][N // 2 - j] = 1


def set_stone(r, c, color):                                         # 돌을 놓는 함수
    board[r][c] = color                                             # 해당 좌표에 돌을 놓는다
    check_stone(r, c, color)                                        # 뒤집을 돌을 확인하는 함수로 이동


def check_stone(r, c, color):                                       # 뒤집을 돌을 확인하는 함수로 이동
    dr = [-1, -1, -1, 1, 1, 1, 0, 0]                                # 8방탐색
    dc = [-1, 1, 0, -1, 1, 0, -1, 1]
    for k in range(8):
        change = set()                                              # 뒤집을 수 있는 돌의 후보를 저장하는 변수
        for i in range(1, N):                                       # 자신의 다음 돌부터 끝까지 확인
            nr = r + dr[k]*i
            nc = c + dc[k]*i
            if nr < 0 or nr >= N or nc < 0 or nc >= N:              # 범위를 벗어나면
                break                                               # 다음 방향으로
            if board[nr][nc] != color and board[nr][nc] != 0:       # 다른 색이면
                change.add((nr, nc))                                # 바꾸는 후보에 넣는다
            elif board[nr][nc] == color:                            # 같은 색이면
                reverse_stone(change, color)                        # 돌을 뒤집는 함수로 이동
                break                                               # 일자로 확인 종료
            elif board[nr][nc] == 0:                                # 비어있으면
                break                                               # 다음 방향으로


def reverse_stone(arr, color):                                      # 돌 색을 바꾸는 함수
    for r, c in arr:                                                # 지나온 다른 색 돌의 좌표를 하나씩 가져와서
        board[r][c] = color                                         # 자신의 색으로 바꾸기


def count_stone():                                                  # 색별 돌의 개수를 세는 함수
    black = 0                                                       # 검은 돌의 수
    white = 0                                                       # 흰 돌의 수
    for i in range(N):                                              # 배열 전체를
        for j in range(N):                                          # 순환하여서
            if board[i][j] == 1:                                    # 검은 돌이면
                black += 1                                          # 검은 돌의 수 +1
            elif board[i][j] == 2:                                  # 흰 돌이면
                white += 1                                          # 흰 돌의 수 +1
    return black, white                                             # 검은 돌과 흰 돌의 수 반환


for tc in range(int(input())):
    N, M = map(int, input().split())

    board = [[0]*N for _ in range(N)]

    setting()

    for _ in range(M):                                              # 바둑돌을 하나씩 입력 받음
        stone_c, stone_r, stone_color = map(int, input().split())   # 좌표와 색(입력값의 좌표를 주의해야함)
        set_stone(stone_r-1, stone_c-1, stone_color)                # 좌표는 인덱스를 맞추기 위해 -1씩 해줌
    result = count_stone()                                          # 검은 돌의 수와 흰 돌의 수를 튜플로 저장
    
    print(f'#{tc+1}', *result)

