# 갈림길 최대 2개
# A -> B 가는 길이 존재하는지 알아내는 프로그램
# A = 0, B = 99 고정
# 단방향

# 입력
for _ in range(10):                                     # 총 10번 실행
    tc, e = map(int, input().split())                   # tc번호 간선의 개수
    adj_list = [[] for _ in range(100)]                 # 인접리스트를 저장할 리스트 인덱스: 0~99 고정
    data_list = list(map(int, input().split()))         # 입력값을 분할해서 리스트로 저장

    for i in range(0, len(data_list)-1, 2):             # 짝수 인덱스는 출발지, 홀수 인덱스는 도착지 -> 출발지만 뽑기
        adj_list[data_list[i]].append(data_list[i+1])   # 출발지 -> 도착지 단방향 연결

    stack = [0]     # 출발지는 0 고정
    visited = []
    result = 0

    while stack:
        now_location = stack.pop()                    # 갈수 있는 곳 가져오기
        if now_location not in visited:               # 방문한 곳이 아니면
            visited.append(now_location)              # 방문한 곳으로 확인

        for next_location in adj_list[now_location]:  # 현재 위치에서 갈 수 있는 곳 찾기
            if next_location not in visited:          # 방문한 곳이 아니라면
                stack.append(next_location)           # 갈 수 있는 곳을 스택에 저장

    if 99 in visited:
        result = 1
    print(f'#{tc} {result}')
