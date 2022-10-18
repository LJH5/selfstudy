# 파리퇴치
T = int(input())                                                        # tc
for tc in range(1, T+1):                                                # tc만큼 반복
    n, m = map(int, input().split())                                    # n: 파리 영역 크기, m: 파리채 크기
    fly_matrix = [list(map(int, input().split())) for _ in range(n)]    # 파리 분포
    max_kill = 0                                                        # 최대로 죽인 파리 수 저장할 변수

    for y in range(n-m+1):                          # 파리채를 파리 영역에서 순환시킨다
        for x in range(n-m+1):                      # 파리채의 최대 이동 거리는 n-m+1
            sum_fly = 0                             # 파리채 안의 파리의 수를 저장할 변수
            for i in range(y, y+m):                 # 파리채 안의 요소를 순환해서 파리 수를 더한다
                for j in range(x, x+m):             # 파리채 영역의 이동거리는 y~y+m, x~x+m
                    sum_fly += fly_matrix[i][j]     # 영역안의 파리를 다 더해서 최대보다 크면 갱신
            if sum_fly > max_kill:                  # 최대로 죽인 것보다 크면
                max_kill = sum_fly                  # 갱신

    print(f'#{tc} {max_kill}')