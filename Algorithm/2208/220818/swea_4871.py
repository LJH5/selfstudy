T = int(input())
for tc in range(1, T+1):
    result = 0

    # 노드 수 v, 간선 수 e
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]  # 0~6 까지
    # 간선
    for _ in range(e):
        start, end = map(int, input().split())
        adj_list[start].append(end)
    # 출발지 s, 도착지 g
    s, g = map(int, input().split())

    stack = [s]     # 출발지 저장
    visited = []
    while stack:
        now_location = stack.pop()          # 갈수 있는 곳 가져오기
        if now_location not in visited:     # 방문한 곳이 아니면
            visited.append(now_location)    # 방문한 곳으로 확인

        for next_location in adj_list[now_location]:    # 현재 위치에서 갈 수 있는 곳 찾기
            if next_location not in visited:            # 방문한 곳이 아니라면
                stack.append(next_location)             # 갈 수 있는 곳을 스택에 저장

    if g in visited:
        result = 1
    print(f'#{tc} {result}')