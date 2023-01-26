# x*y 크기의 사각형 x: 가로, y: 세로
# tc
# 0: 가로, 1: 세로
# 0 3 은 좌표 3에서 가로로 자르기
# 자르고 난 뒤 가장 큰 종이 조각의 넓이를 출력
# 가로를 모두 자르기를 실행해서 큰 거
# 세로를 모두 자르기를 실행해서 큰 거

def max_gap(arr):   # 다음 숫자와 비교하여 최대 공백 찾기
    max_len = 0
    for i in range(len(arr)-1):
        if max_len < arr[i+1] - arr[i]:
            max_len = arr[i+1] - arr[i]
    return max_len
x, y = map(int, input().split())
tc = int(input())
# 뚜껑 열기
sero_cut = [0]         # 세로로 자르기
garo_cut = [0]         # 가로로 자르기
for i in range(tc):
    check, r = map(int, input().split())
    if check:
        sero_cut.append(r)
    else:
        garo_cut.append(r)
# 뚜껑 닫기
sero_cut.append(x)
garo_cut.append(y)
# 오름차순 정렬
garo_cut.sort()
sero_cut.sort()
# 최대 공백 구하기
max_y = max_gap(garo_cut)
max_x = max_gap(sero_cut)

print(max_y*max_x)