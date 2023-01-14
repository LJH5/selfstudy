import sys
input = sys.stdin.readline


N = int(input())

adj = [[] for _ in range(N+1)]
for i in range(N-1):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

stack = [[1, 0]]
visited = [0] * (N+1)
move = []

while stack:
    n, cnt = stack.pop()
    visited[n] = 1

    if n != 1 and len(adj[n]) == 1:     # 루트노드가 아니면서 리프노드 일때
        move.append(cnt)                # 누적 카운터 더하기
        continue

    for nn in adj[n]:                   # 다음으로 갈 수 있는 노드
        if visited[nn] == 0:            # 방문한 노드가 아니면
            stack.append([nn, cnt+1])   # 스택에 추가, 누적 카운터 + 1


# print(move)

if sum(move) % 2:
    print('Yes')
else:
    print('No')