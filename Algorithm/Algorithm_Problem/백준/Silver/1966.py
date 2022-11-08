# 프린터 큐
# 중요도가 높을 수록 중요한 문제이다
# 인덱스만 바꾸면 되려나?

for _ in range(int(input())):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(x for x in range(N))

    q = list(zip(imp, idx))
    cnt = 0
    while q:
        max_num = max(q)[0]
        num = q.pop(0)
        if num[0] == max_num:
            if num[1] == M:
                result = cnt
                break
        else:
            cnt += 1
            q.append(num)

    print(result)