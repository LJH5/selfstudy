n = int(input())    # 색종이의 개수 n
xy_arr = []         # 색종이의 좌표를 저장하는 리스트
matrix = [[0]*1001 for _ in range(1001)]
result_list = [0]*n
for i in range(n):
    xy_arr.append(list(map(int, input().split())))

for i in range(n):                             # 좌표의 영역을 메트릭스에 표시 1은 1로... 4는 4로
    x = xy_arr[i][0]
    y = xy_arr[i][1]
    x_len = xy_arr[i][2]
    y_len = xy_arr[i][3]

    for j in range(y, y+y_len):                     # 사각형 구하기
        for k in range(x, x+x_len):
            if matrix[j][k] == 0:
                matrix[j][k] = i+1
                result_list[i] += 1
            else:
                result_list[matrix[j][k] - 1] -= 1  # 겹치는 영역이면 이전 총합에서 빼줌
                matrix[j][k] = i + 1  # 영역을 +1씩 해준다
                result_list[i] += 1

for i in range(n):              # 출력 for 하나만 써야 된다!!
    print(result_list[i])