# 덩치
n = int(input())
size = [list(map(int, input().split())) for _ in range(n)]
grade = [0]*n
rank = 1

for i in range(n):
    tmp_x = size[i][0]
    tmp_y = size[i][1]
    rank = 1
    for j in range(n):
        if tmp_x < size[j][0] and tmp_y < size[j][1]:
            rank += 1
    grade[i] = rank

print(*grade)