# 파스칼 삼각형
# 처음은 1이 나온다
# 다음은 1 1이 나온다
# 다음 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    stack = []
    for i in range(N):
        result = [1]
        for _ in range(len(stack)):
            result.append(stack.pop())
        print(*result)

        stack.append(1)
        if N > 2:
            for i in range(len(result)-1):
                stack.append(result[i] + result[i+1])
