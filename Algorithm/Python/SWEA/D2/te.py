import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(9)]
    # box = [[]*3 for _ in range(3)]     # 굳이? 만들어야되나
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(arr)
    # print(box)

    row_list = []
    for r in range(9):                              #가로를 하나씩 출력해야된느데
        tmp_list = []
        for c in range(9):
            tmp_list.append(arr[r][c])
        row_list.append(list(set(tmp_list)))

    # print(row_list)

    col_list = []
    for r in range(9):
        tmp_list = []
        for c in range(9):
            tmp_list.append(arr[c][r])
        col_list.append(list(set(tmp_list)))

    # print(col_list)

    box_list = []
    for r in range(3):
        for c in range(3):
            tmp_list = []
            for i in range(r*3, (r*3)+3):
                for j in range(c*3, (c*3)+3):
                    tmp_list.append(arr[i][j])
            # print(box_list)
            box_list.append(list(set(tmp_list)))
            # print(box_list)
            # if arr[r][c] != arr[r+1][c] or arr[r][c] != [r][c+1]:
            # box_list.append(list(arr[r][c]))
            # box_list.append(list(arr[c][r]))
    # print(box_list)
    # else:
    #     continue
    #     # print(num_box)
    result = 1
    for i in range(9):
        if len(row_list[i]) != 9 or len(col_list[i]) != 9 or len(box_list[i]) != 9:
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')

    # if len(num) == len(row_list) and len(num) == len(col_list) and len(num) == len(box_list):
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')