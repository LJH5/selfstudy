# N을 +1, -1, *2, -10 네 가지를 이용해서 M을 만드는 최소 횟수
# 그래프를 만들어서
# 자연수니까 0 이하로 내려가면 버리고
# 같은 값이 나오면 길을 이어준다
# N의 값을 각각 구해서
def way(now, cnt):
    global result
    if cnt > result:
        return
    if now == M:
        if cnt < result:
            result = cnt
            return

    if (now, now*2) not in graph:
        graph.extend((now, now*2))
        way(now * 2, cnt + 1)

    if (now, now + 1) not in graph:
        graph.extend((now, now+1))
        way(now + 1, cnt + 1)

    if (now, now - 1) not in graph:
        graph.extend((now, now - 1))
        way(now - 1, cnt + 1)

    if (now, now - 10) not in graph:
        graph.extend((now, now - 10))
        way(now - 10, cnt + 1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = M-N
    graph = []
    way(N, 0)
    print(f'#{tc} {result}')
