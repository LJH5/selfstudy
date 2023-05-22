def find_coordinates():                     # '#'인 좌표를 저장하는 함수
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '#':
                coordinates.add((i, j))


def find_point(arr):                        # '#'의 좌표 중에서 최소 좌표와 최대 죄표를 찾는 함수
    min_r, min_c = min(arr)
    max_r, max_c = max(arr)
    return (min_r, min_c), (max_r, max_c)


def check():                                # 정사각형인지 판정하는 함수
    min_r, min_c = min_coord
    max_r, max_c = max_coord
    if max_r - min_r != max_c - min_c:      # 두 변의 길이가 다르면 정사각형이 아님
        return 'no'
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if matrix[r][c] != '#':         # 사각형 사이에 '#'이 아닌 것이 있으면 안됨
                return 'no'
    return 'yes'


for tc in range(int(input())):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    coordinates = set()
    result = 'no'
    find_coordinates()
    # 좌상단의 좌표와 우하단의 좌표
    min_coord, max_coord = find_point(coordinates)
    result = check()

    print(f'#{tc+1} {result}')