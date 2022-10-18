v, e = map(int, input().split())
# 비어 있는 2차원 배열을 만든다
adj_matrix = [[] for _ in range(v+1)]

# 각 출발지에서 도착할 수 있는 도착지 만 넣는다
# 예) [[], [2, 3], ...]
for _ in range(e):
    start, end = map(int, input().split())
    adj_matrix[start].append(end)
    adj_matrix[end].append(start)       # 양방향 그래프

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
    # des는  current에서 갈 수 있는 도작지가 나온다
    for des in adj_matrix[current]:
        if des not in visited:
            stack.append(des)

print(*visited)