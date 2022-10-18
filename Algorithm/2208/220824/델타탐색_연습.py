# 입력받은 좌표의 의 상,하,좌,우 합을 구하시오
# 입력받은 좌표를 델타탐색을 이용하여 합을 구한다!
arr = [[3, 5, 4],
       [1, 1, 2],
       [1, 3, 9]]
y, x = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

sum = 0
# 델타 탐색
# y, x의 상하좌우를 살핀다.
for k in range(4):
    new_r = dr[k] + y
    new_c = dc[k] + x
    # 이때 주의해야할 것은 arr의 인덱스를 벗어나면 안 된다.
    if new_c < 0 or new_c >= len(arr) or new_r < 0 or new_r >= len(arr):
        continue
    sum += arr[new_r][new_c]

print(sum)
