matrix = [[0]*100 for i in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):         # 사각형 씩 구하기
        for j in range(x1, x2):
            matrix[i][j] = 1        # 사각형 영역에 1 저장(겹치는 영역도 1로 저장됨)
result = 0
for i in matrix:                    # 2차원 배열에서 1의 개수 구하기
    result += i.count(1)
print(result)
