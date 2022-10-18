# 어차피 완전이진트리니까 순서는 정해져있음

#중위 순회
def inorder(n):
    global result
    if n <= size:
        inorder(2*n)
        result += tree[n]
        inorder(2*n+1)

for tc in range(1, 11):
    result = ''
    tree = [0]                      # 입력값의 문자만 저장할 배열
    n = int(input())
    for i in range(n):
        txt = input().split()[1]    # 입력값은 문자(실질적으로 출력할 것)
        tree.append(txt)            # 배열에 저장
    size = len(tree) - 1

    inorder(1)
    print(f'#{tc} {result}')
