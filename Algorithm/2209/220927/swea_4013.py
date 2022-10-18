import sys
sys.stdin = open('input.txt', 'r')
# 자석은 4개, 자석 당 날의 수는 8개
# K: 회전 횟수
# 회전할 자석의 번호와 회전 방향
# 자석을 회전하였을 때 옆의 자석이 다르면 반대 방향으로 회전
# 시계방향이면 0번을 끝으로
# 반시계방향이면 끝번을 0으로

def ro_right(n):
    mg[n].insert(0, mg[n].pop())

def ro_left(n):
    mg[n].append(mg[n].pop(0))


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mg = [[0] + list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        mg_num, ro_dir = map(int, input().split())
        if ro_dir == 1:
            for i in range(4):
                if i == mg_num:
                    ro_right(i)
                if mg_num:
                    pass
        else:
            pass
    print(f'#{tc}')
