import sys; sys.stdin = open('10988.txt')

# 카운팅을 해도 무방하지만
# 중복을 제거하고, 크기순으로 자료에 접근하기 위해
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 값의 범위 => 1 ~ 1000
    cnt = [0] * (1001)

    for val in arr:
        cnt[val] = 1

    ans = kth = 0
    for i in range(1, 1001): # 1 ~ 1000 까지 숫자
        if cnt[i]:
            kth += 1
            if kth == K:
                # i를 출력
                ans = i
                break

    print(ans)

