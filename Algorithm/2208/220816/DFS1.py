# 0으로 초기화한 2차원 배열로 경로를 자료 구조화
# (주의: 단방향/양방향, 인덱스는 0~vertex, 길이는 vertex+1)
# stack, visited 만들기
v, e = map(int, input().split())
adj_matrix = [[0]*(v+1) for _ in range(v+1)]
# 간선의 개수 만큼 반복
for _ in range(e):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1      # 양방향이니까

stack = [1]     # 시작점 부터 가니까
visited = []

while stack:
    current = stack.pop()
    # 방문하지 않은 곳이라면 추가
    if current not in visited:
        visited.append(current)

    for des in range(v+1):
        # 갈 수 있는 곳이 있고 방문하지 않은 곳이라면
        if adj_matrix[current][des] and des not in visited:
            stack.append(des)