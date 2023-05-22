import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
# v: 노드의 개수, e: 간선의 개수
def bfs(arr, s, v):
    global result
    q = deque([s])
    v.append(s)
    cnt = 0
    while q:
        size = len(q)
        for _ in range(size):        # while 안에 pop이 하나있으면 하나씩 뽑히기 때문에 형제를 묶을 수 없다
            now = q.popleft()        # 형제들은 묶어서 싸그리 뽑아야한다
            if g == now:
                result = cnt
                break
            for des in arr[now]:
                if des not in visited:
                    q.append(des)
                    visited.append(des)
        cnt += 1
T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]
    for _ in range(e):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)
    s, g = map(int, input().split())
    visited = []
    result = 0
    bfs(adj_list, s, visited)
    print(f'#{tc} {result}')