# N: 정원의 길이, D: 스프링쿨러의 거리
# 물을 주는 것은 좌우 + 스프링쿨러 자리 => D + 1
T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    wt = 2*D+1           # 하나의 스프링쿨러 범위
    result = N // wt    # 스프링쿨러 범위 안 겹치게 놓았을 때의 수
    if N % wt > 0:       # 안 겹치게 놓았을 때 커버 못하면
        result += 1      # 스프링쿨러 하나 추가

    print(f'#{tc} {result}')