T = int(input())
# 1개 짜리
for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}')
    if n > 0:
        print(1)
    stack = [1]
    for i in range(2, n + 1):
        # 파스칼은 stack.append(1)
        stack.append(1)
        pascal_triangle = stack
        print(*pascal_triangle)

        # 파스칼의 더한 값 stack에 넣기
        stack = [1]
        for j in range(i - 1):
            tmp_sum = pascal_triangle[j] + pascal_triangle[j + 1]
            stack.append(tmp_sum)
