# 400개의 방
# 위에 200개
# 아래 200개
# 방의 번호는 1번부터
# 구간이 겹치면 1 만큼 기다려야 한다
# N 은 돌아가야할 학생의 수
# 현재방, 돌아가야할 방
# 도착 방 번호가 출발 방번호 - 1 이면 대기해야함
# 번호가 높은 방에서 낮은 방으로 갈 때도 처리해야함
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [0] * 201
    for i in range(N):
        st, ed = map(int, input().split())
        if st < ed:
            st = (st + 1) // 2
            ed = (ed + 1) // 2
        else:
            st, ed = (ed+1) // 2, (st + 1) // 2
        for j in range(st, ed + 1):
            room[j] += 1
    result = max(room)
    print(f'#{tc} {result}')