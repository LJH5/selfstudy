T = int(input())
for tc in range(1, T+1):
    result = []                             # 결과를 저장할 리스트
    N = int(input())                        # N은 노선의 개수
    bus = []                                # 버스의 노선을 저장할 리스트
    for i in range(N):                      # 노선의 개수만큼 반복
        A, B = map(int, input().split())    # A는 시발점, B는 종점
        bus.append((A, B))                  # 리스트에 튜플형태로 저장
    P = int(input())                        # P는 정류장의 개수
    for i in range(P):                      # 정류장의 개수만큼 반복
        C = int(input())                    # 정류장의 위치
        cnt = 0                             # 해당 정류장을 지나는 노선의 개수
        for A, B in bus:                    # A는 시발점, B는 종점
            if A <= C <= B:                 # 정류장이 시발점과 종점 사이에 있으면
                cnt += 1                    # 해당 정류장을 지나는 노선의 개수 + 1
        result.append(cnt)                  # 각각 정류장을 지나는 노선의 개수를 리스트에 저장
    print(f'#{tc}', *result)