import sys
def find_set(x):
    if p[x] != x:               # 자신이 보스가 아니면
        p[x] = find_set(p[x])   # 자신의 보스를 찾아 올라가서 저장
    return p[x]

V, E = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
p = []
for i in range(V+1):
    p.append(i)

# 거리 최소 순으로 정렬
edges.sort(key=lambda x:x[2])
result = 0
cnt = 0
for x, y, w in edges:
    x_rt, y_rt = find_set(x), find_set(y)
    if x_rt != y_rt:
        if x_rt < y_rt:
            p[y_rt] = x_rt
        else:
            p[x_rt] = y_rt
        cnt += 1
        result += w

        if cnt == V:
            break
# print(p)
print(result)
