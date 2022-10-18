# 5*5 숫자판
# 자기가 간 곳의 지나간 곳의 숫자를 붙여 씀
# 중복되지 않는 숫자의 조합은 몇개인가?
# (0,0)부터 dfs?
# 다음으로 갈수 있는 곳을 사방탐색한다
# 한칸 이동후 밟은 곳을 visted에 넣는다
# 반복하다가 depth가 5가되면 사용하지 않은 조합일 시 check에 저장하고, +1 해준다
# 한칸 되돌아가서 사방탐색
def dfs(r, c, visit):
    visit += matrix[r][c]
    if len(visit) == 6:                         # 6칸 방문했을 때
        if visit not in result:                 # 새로운 조합이라면
            result.add(visit)                   # 저장
        return
    for k in range(4):                          # 사방탐색
        new_r = r + dr[k]
        new_c = c + dc[k]
        if 0 <= new_r < 5 and 0 <= new_c < 5:   # 유효한 index라면
            dfs(new_r, new_c, visit)


matrix = [list(input().split()) for _ in range(5)]
result = set()
# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(5):          # 시작점을 바꾸어 준다
    for j in range(5):
        dfs(i, j, '')

print(len(result))