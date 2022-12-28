def make_set(x):
    p[x] = x


def find_set(x):  # 효율성이 고려된 find set
    if p[x] != x:
        p[x] = find_set(p[x])  # path compression
    return p[x]


def union(x, y):  # Union 그룹 합치기 -> 그룹내 모든 값 바꿈
    link(find_set(x), find_set(y))  # 대표끼리 링크!


def link(x, y):  # 랭크가 다른 트리 합치는 것
    if r[x] > r[y]:  # x 쪽 랭크가 큰 경우에는
        p[y] = x  # y를 x에 흡수시킴
    else:
        p[x] = y  # 아닌 경우는 반대긴 한데
        if r[x] == r[y]:  # 같으면?
            r[y] += 1  # y 랭크를 하나 올려줌


V = int(input())
E = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]
p = [0]*(V+1)  # 0 ~ V 번까지 있으니까 V+1 개
r = [0]*(V+1)  # 랭크 표시용

for i in range(V+1):
    make_set(i)  # list(range(V+1))과 같음

cnt = 0  # 간선 선택 횟수

for x, y in edges:  # 대표자 같으면 다음으로 걍 넘어감
    if find_set(x) != find_set(y):  # 대표자가 다른경우에만
        union(x, y)  # union 해주고
        cnt += 1

    if cnt == V:  # V-1 개까지만 선택해야 하니까!
        break


print(p.count(p[1]) - 1)