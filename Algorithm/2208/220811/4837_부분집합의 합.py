T = int(input())
for tc in range(1, T+1):
    A = [i for i in range(1, 13)]
    N, K = map(int, input().split())
    bubunjiphap_count = 0
    for i in range(1 << len(A)):
        bubunjiphap = []
        for j in range(len(A)):
            if i & (1 << j):
                bubunjiphap.append(A[j])
        if len(bubunjiphap) == N and sum(bubunjiphap) == K:
            bubunjiphap_count += 1
    print(f'#{tc} {bubunjiphap_count}')
