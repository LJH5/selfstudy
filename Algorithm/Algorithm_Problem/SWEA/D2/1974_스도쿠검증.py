# 스도쿠라면 1을 출력
# 한줄, 사각형 하나를 set으로 중복을 제거하였을 때 길이가 9
T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    # 사각형 스도쿠의 좌상단 좌표
    squr = [(0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)]
    for i in range(9):
        # 가로
        if len(set(sudoku[i])) != 9:
            break

        # 세로
        tmp = set()
        for j in range(9):
            tmp.add(sudoku[j][i])
        if len(tmp) != 9:
            break

        # 사각형
        y, x = squr[i]
        tmp2 = set()
        for r in range(y, y+3):
            for c in range(x, x+3):
                tmp2.add(sudoku[r][c])
        if len(tmp2) != 9:
            break
    else:
        result = 1

    print(f'#{tc} {result}')