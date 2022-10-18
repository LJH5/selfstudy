import sys
sys.stdin=open('input.txt')
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]  # 문제에서 정해준 방향
dc = [0, 1, 0, -1]
current = (r, c)  # 시작위치
cleaned = set()
while True:

    cleaned.add(current)  # 현위치 청소
    for i in range(4):  # 네 방향 탐색
        new_d = (d - 1 - i) % 4  # 현재기준으로 윈쪽(d-1)을 보고 계속 왼쪽으로 회전
        if board[current[0] + dr[new_d]][current[1] + dc[new_d]] == 0 and\
                (current[0] + dr[new_d], current[1] + dc[new_d]) not in cleaned:  # 갈 수 있으며 아직 청소 안했다면
            current = (current[0] + dr[new_d], current[1] + dc[new_d])  # 간다!

            d = new_d  # 바라보는 방향 유지
            print(current, d)
            break
    else:  # 네 방향을 모두 봤는데 갈 곳이 없다면
        if board[current[0]-dr[d]][current[1]-dc[d]]:  # 후진 못하면 끝
            break
        current = (current[0]-dr[d], current[1]-dc[d])  # 후진 가능시 후진
print(len(cleaned))