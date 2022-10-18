import sys
sys.stdin = open("input.txt", "r")

# N: 컨테이너 수, M: 트력의 수
# A에서 B 지역으로 이동할 때 
# 트럭당 한 개의 컨테이너를 운반
# 적재용량을 초과하면 운반할 수 없음
# 다음줄은 컨테이너의 무개
# 다음줄은 트럭의 적재 용량
# 운반한 총 무개가 최대가 되도록 하라
# N개 중에서 M개 고르기 조합?
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container_weight = list(map(int, input().split()))
    truck_capacity = list(map(int, input().split()))
    result = 0
    
    container_weight.sort(reverse=True)                     # 오름차순 정렬
    truck_capacity.sort(reverse=True)                       # 오름차순 정렬

    for i in range(M):                                      # 트럭 적재용량이 큰 것 부터
        for j in range(N):                                  # 컨테이너의 무게가 무거운 것 부터
            if truck_capacity[i] >= container_weight[j]:    # 트럭의 적재용량이 컨테이너의 무게보다 크면
                result += container_weight[j]               # 운송한 무게에 추가
                container_weight[j] = 99999                 # 이미 운송한 컨테이너의 무게룰 제외하기 위해
                break
    

    print(f'#{tc} {result}')