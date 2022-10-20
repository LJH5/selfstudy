# 도시분할계획
import sys

def make_set(x):
    p[x] = x                    # p에 자기 자신을 저장

def find_set(x):
    if p[x] != x:               # 자신이 보스가 아니면
        p[x] = find_set(p[x])   # 자신의 보스를 찾아 올라가서 저장
    return p[x]

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    if r[x] > r[y]:
        p[y] = x
    else:
        p[x] = y
        if r[x] == r[y]:
            r[y] += 1

V, E = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
p = [0] * (V+1)
r = [0] * (V+1)
for i in range(V+1):
    make_set(i)
# 거리 최소 순으로 정렬
edges.sort(key=lambda x:x[2])
result = 0
cnt = 0
for x, y, w in edges:
    if find_set(x) != find_set(y):  # 서로 보스가 다르다 = 연결 되어있지 않다
        union(x, y)                 # 연결
        result += w                 # 연결 비용 더하기
        cnt += 1                    # 연결 횟수 증가

    if cnt == V-2:
        break

print(p[1:])
print(result)
