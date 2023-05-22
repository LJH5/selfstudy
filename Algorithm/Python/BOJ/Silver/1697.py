from collections import deque


def bfs(start):
    q = deque([start])
    visited = set()
    cnt = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            if now == k:
                return cnt
            if now in visited:
                continue
            visited.add(now)
            for nxt in (now - 1, now + 1, 2 * now):
                if 0 <= nxt < 100001 and nxt not in visited:
                    q.append(nxt)
        cnt += 1


n, k = map(int, input().split())
print(bfs(n))