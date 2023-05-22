t = int(input())
for tc in range(t):
    N = int(input())
    farm = [input() for _ in range(N)]
    # print(farm)

    harvest = []

    for i in range(N):
        if i == N//2:
            harvest.append(farm[i][:])
        if i < N//2:
            harvest.append(farm[i][N//2-i:N//2+i+1])
        if i > N//2:
            harvest.append(farm[i][N//2-(N-i)+1:N//2+(N-i)])

    # print(harvest)
    real_harvest = []
    for i in harvest:
        real_harvest.append(list(i))
    # print(real_harvest)
    ans = 0
    for i in range(len(real_harvest)):
        for j in range(len(real_harvest[i])):
            ans += int(real_harvest[i][j])
    print(f'#{tc+1} {ans}')