matrix = [[0]*100 for _ in range(100)]  # 100x100 행렬
# 도화지는 10x10 고정
# 입력 좌표는 좌하단 꼭지점
tc = int(input())
cnt = 0                                 # 영역 개수를 저장
for _ in range(tc):                     # 입력 개수만큼 반복
    x, y = map(int, input().split())    # 좌하단 꼭지점
    for i in range(y, y+10):            
        for j in range(x, x+10):
            if matrix[i][j] == 0:       # 입력되지 않은 곳이라면
                matrix[i][j] = 1        # 1을 넣고
                cnt += 1                # 영역 개수 +1

print(cnt)