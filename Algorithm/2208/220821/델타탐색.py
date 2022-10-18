# 델타 탐색
# 이차원 배열에서 해당인덱스의 상하좌우의 인덱스를 확인
# row 행, column 열
# 상: 행-1, 하: 행+1, 좌: 열-1, 우: 열+1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 5의 인덱스는 [2][2]
# 5의 상에 위치한 2의 인덱스는 [1][2]
# 즉 [2 + (-1)][2 + 0] dr[0]과 dc[0]
r = 2
c = 2
new_r = r + dr[0]
new_c = c + dc[0]
# dr[k], dc[k]에서 k가 0: 상, 1: 하, 2: 좌, 3: 우

# arr안 모든 요소의 상하좌우를 탐색하고 싶다면
for r in range(len(arr)):
    for c in range(len(arr[r])):
        for k in range(4):
            new_r = r + dr[k]
            new_c = c + dc[k]
