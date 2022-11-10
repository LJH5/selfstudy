# 비용을 나타내는 2차원 배열이 있을때
# +로 피는 꽃을 겹치는 부분이 없이 심을 때
# 최소비용을 구하여라
# 씨앗은 총 3개
# 일단 씨앗을 심을 수 있는 영역은 1~N-1
import sys


def bloom(r, c):    # 씨앗을 좌표를 받고 꽃이 피는 영역을 구함
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    flower_bloom = [(r, c)]
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        flower_bloom.append((nr, nc))

    return flower_bloom


def plant_sow():    # 씨앗이 심어지는 위치
    total_flower_bloom = []
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            total_flower_bloom.append(bloom(r, c))

    return total_flower_bloom


def combination():  # 조합으로 3개 뽑기
    flower = plant_sow()
    n = len(flower)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                total_flower = flower[i] + flower[j] + flower[k]
                if set_check(total_flower, 15):
                    cost = cal_cost(total_flower)
                    check_min_cost(cost)


def set_check(arr, length): # 꽃잎이 겹치는 영역이 있는지 확인
    if len(set(arr)) == length:
        return True
    else:
        return False


def cal_cost(arr):  # 꽃이 피는 영역의 비용을 계산
    cost = 0
    for r, c in arr:
        cost += field[r][c]
    return cost


def check_min_cost(cost):   # 최소비용인지 확인
    global result
    if cost < result:
        result = cost


N = int(input())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 이게 되는구나... 뒤에 input이 먼저 실행되는 구나
result = 9999
combination()

print(result)