def dfs(now):
    global result
    if now not in visited:
        visited.append(now)

    for des in adj_list[now]:
        if des not in visited:
            result += 1
            dfs(des)

for tc in range(int(input())):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    result = 0
    for _ in range(M):                              # 인접리스트 만들기
        start, end = map(int, input().split())      # 출발지와 도착지 경로를 입력받고
        adj_list[start].append(end)                 # 경로를 연결
        adj_list[end].append(start)                 # 왕복으로 연결
    visited = []                                    # 방문한 곳을 확인할 것
    dfs(1)
    print(result)