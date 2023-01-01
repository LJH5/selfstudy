from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def make_ajx_list():
    ajx_list = defaultdict(list)
    for _ in range(E):
        s, e = map(int, input().split())
        ajx_list[s].append(e)
        ajx_list[e].append(s)
    return ajx_list


def dfs(arr, start_node):
    visited = []
    stack = [start_node]

    while stack:
        now = stack.pop()
        if now in visited:
            continue
        visited.append(now)
        for next_node in sorted(arr[now], reverse=True):    # 방문 순서 보정
            if next_node in visited:
                continue
            stack.append(next_node)
    return visited


def bfs(arr, start_node):
    visited = []
    q = deque([start_node])
    while q:
        now = q.popleft()
        if now in visited:
            continue
        visited.append(now)
        for next_node in sorted(arr[now]): # 순서 보장
            if next_node in visited:
                continue
            q.append(next_node)
    return visited


V, E, S = map(int, input().split())
ajx_list = make_ajx_list()

dfs_visit = dfs(ajx_list, S)
bfs_visit = bfs(ajx_list, S)

print(*dfs_visit)
print(*bfs_visit)