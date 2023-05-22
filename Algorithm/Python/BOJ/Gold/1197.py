import sys
from collections import defaultdict
from heapq import *
input = sys.stdin.readline


def prim(start_node, edges):
    mst = []                                              # 최소 신장 트리를 저장할 리스트
    adjacent_edges = defaultdict(list)                    # 자동으로 dict 구조를 만들어줌, 비어있는 키는 빈 리스트로 만듬
    for s, e, d in edges:                                 # 해당 노드에 해당 간선을 추가
        adjacent_edges[s].append((d, s, e))
        adjacent_edges[e].append((d, e, s))
    print('adjacent_edges:', adjacent_edges)
    connected = set()                                     # 연결된 노드를 저장할 set
    connected.add(start_node)                             # 처음 선택한 노드를 연결된 노드 집합에 삽입
    candidated_edge = adjacent_edges[start_node]          # 시작노드와 연결된 간선들을 후보에 삽입
    print('시작노드 포함 간선 후보:', candidated_edge)
    heapify(candidated_edge)                              # 오름 차순으로 정렬
    print('candidated_edge 정렬:', candidated_edge)
    while candidated_edge:                                # 모두 연결할때까지 반복
        print('----------------------------------')
        # print('후보 간선:', candidated_edge)
        d, s, e = heappop(candidated_edge)
        if e not in connected:                            # 사이클 있는지 확인 후
            connected.add(e)                              # 사이클이 없으면 연결
            mst.append((d, s, e))                         # 최소 신장트리에 거리 최소인 간선 삽입

            for edge in adjacent_edges[e]:                # 다음으로 갈수 있는 노드 탐색
                print(f'{e}번 노드와 연결된 간선들: {edge}')
                if edge[2] not in connected:              # 다음으로 갈 수 있는 노드 중 사이클이 발생하는 지 확인
                    heappush(candidated_edge, edge)       # 사이클이 발생하지 않으면 후보에 등록

    return mst


V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

MST = prim(1, edges)
print('=====결과==========================')
print('Prim MST')
result = 0
for d, s, e in MST:
    result += d
    print(f'출발: {s}, 도착: {e}, 비용: {d}')
print('최소 비용:', result)