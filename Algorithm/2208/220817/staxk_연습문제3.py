v, e = map(int, input().split())
adj_list = [[] for _ in range(v + 1)]               # 인접리스트를 저장할 리스트 인덱스: 0~7
data_list = list(map(int, input().split()))         # 입력값을 분할해서 리스트로 저장

for i in range(0, len(data_list)-1, 2):             # 짝수 인덱스는 출발지, 홀수 인덱스는 도착지 -> 출발지만 뽑기
    adj_list[data_list[i]].append(data_list[i+1])   # 출발지 -> 도착지 단방향 연결
    adj_list[data_list[i+1]].append(data_list[i])   # 양방향으로 연결

visited = []    # 방문 체크
stack = [1]     # 1부터 시작

while stack:
    now_location = stack.pop()           # 현재위치 뽑기
    if now_location not in visited:      # 현재위치가 방문한 곳이 아니면
        visited.append(now_location)     # 방문한 곳으로 저장

    for next_location in adj_list[now_location][::-1]:      # 다음 방문할 곳 찾기, 큰 수 부터 스택에 넣기
        if next_location not in visited:                    # 현재위치에서 갈 수 있고 방문한 곳이 아니라면
            stack.append(next_location)                     # 스택에 다음으로 갈 곳 넣기

print(*visited)