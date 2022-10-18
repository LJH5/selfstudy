# 모든 길은 이어져있다
# 1번에서 출발하여 각 구역을 한번씩 방문하고 다시 1번으로 돌아온다
# 최소 배터리 소모량을 구하라
# dfs로 풀어야지
import sys
sys.stdin = open('input.txt', 'r')
def dfs(n, acc, depth):
    global result
    if acc > result:                                        # 중간합이 더 크면 뒤는 볼 필요도 없음
        return
    if depth == N:                                          # 모든 곳을 방문 했을 때
        if acc < result:                                    # 최소합이라면
            result = acc                                    # 저장
            return
    for des in range(1, N):                                 # 모든 시작지점은 0이고 도착지점도 0임
        if depth < N-1:                                     # 출발지로 돌아오기 전
            if matrix[n][des] != 0 and visited[des]==0:     # 자기 자신과 방문한 곳이 아니면
                visited[des] = 1                            # visited에 추가
                dfs(des, acc+matrix[n][des], depth + 1)     # 다음 목적지로 이동
                visited[des] = 0                            # 갔가오면 visited 되돌리기
        if depth == N - 1:                                  # 출발지로 돌아오기전
            dfs(0, acc + matrix[n][0], N)                   # 출발지로 도착

T = int(input())
for tc in range(1, T+1):
    result = 99999
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    dfs(0, 0, 0)
    print(f'#{tc} {result}')