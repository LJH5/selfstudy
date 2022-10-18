def sudoku_check(arr):  # 하나의 리스트의 같은 숫자 확인 및 합이 45인지 확인
    dup_check = []               # 중복 확인 리스트
    sum = 0                      # 합을 저장할 변수
    for i in arr:
        if i not in dup_check:   # 같은 숫자x
            dup_check.append(i)  # 중복확인 리스트에 저장
            sum += i
        else:                    # 같은 숫자o
            return False
    if sum == 45:                # 같은 숫자x, 합이 45
        return True

T = int(input())
for tc in range(1, T+1):
    result = 1
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # 가로 검사
    for r in sudoku:
        if not sudoku_check(r):
            result = 0
            break
    # 세로 검사
    sero_sudoku = list(zip(*sudoku))
    for c in sero_sudoku:
        if not sudoku_check(c):
            result = 0
            break
    # 사각형 검사
    flag = True
    cnt = 0
    while cnt < 10 and flag:
        for c in range(0, 7, 3):
            for r in range(0, 7, 3):
                square_sudoku = []
                for y in range(c, c+3):
                    for x in range(r, r+3):
                        square_sudoku.append(sudoku[y][x])
                if not sudoku_check(square_sudoku):
                    result = 0
                    flag = False
                cnt += 1

    print(f'#{tc} {result}')