# 영역 매트릭스를 확힌하여 비교한 것과 패턴이 일치하는지 확인
# 파리퇴치 처럼 풀기?
T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    comp_matrix = []                                # 비교할 리스트를 1차원으로 저장
    for i in range(3):
        for j in map(int, input().split()):
            comp_matrix.append(j)

    same_cnt = 0
    for r in range(n - 2):                           # 전체 영역을
        for c in range(n - 2):                       # 3x3 크기로
            new_matrix = []
            for y in range(r, r+3):                  # 순환하는
                for x in range(c, c+3):              # 코드
                    new_matrix.append(matrix[y][x])  # 3x3 순환을 1차원 리스트로 저장
            if comp_matrix == new_matrix:            # 두 리스트가 같은지 비교
                result += 1

    print(f'#{tc} {result}')