import sys
sys.stdin = open('4831.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # K: 한번 충전으로 이동할 수 있는 정류장 수
    # N: 목적지
    # M: 충전기가 설치된 정류장의 수, 위치
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    station_position = [0 for _ in range(N+1)]


    for i in station:
        station_position[i] += 1

    # 1. 버스가 종점까지 못 가는 경우
    # 충전소 사이의 최대 거리가 K보다 크면
    max_blank = 0
    for i in range(M-1):
        if station[i+1] - station[i] > max_blank:
            max_blank = station[i+1] - station[i]
    if max_blank > K:
        print(f'#{tc}', 0)

    # 2. 버스가 종점까지 갈 수 있는 경우
    else:
        # 버스의 현재 위치
        bus_position = 0
        # 충전 횟수
        charge_cnt = 0
        # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

        # 버스가 목적지에 도착할때까지
        while True:
            # 일단 최대 거리로 이동

            # 도착점을 통과하면
            if bus_position + K >= N:
                bus_position += K
                break

            # 도착점에 충전소가 없으면
            if station_position[bus_position + K] == 0:
                # 출발점과 도착점 사이에 있는 도착점과 가장 가까운 충전소 가기
                for i in range(bus_position + K, bus_position, -1):
                    if station_position[i] == 1:
                        bus_position = i
                        charge_cnt += 1
                        break
            # 도착점에 충전소가 있으면
            else:
                bus_position += K
                charge_cnt += 1

        print(f'#{tc} {charge_cnt}')
