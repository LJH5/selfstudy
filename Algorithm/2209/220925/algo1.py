# 높아지다가 낮아지면 봉우리
T = int(input())
for tc in range(1, T+1):
    result = 0
    N = int(input())
    mt = [0, 0] + list(map(int, input().split())) + [0, 0]
    for i in range(1, N+2):
        if mt[i] > mt[i-1] and mt[i] > mt[i+1]:
            result += 1
        elif mt[i] == mt[i+1] and mt[i+1] > mt[i+2]:
            result += 1


    print(f'#{tc} {result}')