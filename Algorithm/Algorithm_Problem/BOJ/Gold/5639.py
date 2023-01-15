# 입력값은 전위순회
# 출력값은 후위순회
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)            # 재귀 깊이 런타임 에러 방지


def postorder(s, e):
    if s > e:
        return
    mid = e + 1                         # 오른쪽 자식이 없을 경우

    for i in range(s + 1, e + 1):
        if tree[s] < tree[i]:           # 오른쪽 자식 찾기
            mid = i                     # 오른쪽 자식의 인덱스 번호
            break

    postorder(s + 1, mid - 1)           # 왼쪽 자식
    postorder(mid, e)                   # 오른쪽 자식
    print(tree[s])


tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

postorder(0, len(tree) - 1)