# 프린터 큐
# 중요도가 높을 수록 중요한 문제이다
# 인덱스만 바꾸면 되려나?

for _ in range(int(input())):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(x for x in range(N))         # 인덱스의 번호를 만들어줌

    q = list(zip(imp, idx))                 # 우선순위와 인덱스 번호를 튜플로 만들어줌
    cnt = 0                                 # 몇번째로 출력됐는지 수를 세는 변수
    while q:                                # q가 빌때까지 반복
        max_num = max(q)[0]                 # q의 최대값을 저장하는 변수
        num = q.pop(0)                      # q에서 맨앞 하나 뽑아옴
        if num[0] == max_num:               # 만약 최대값과 같으면
            cnt += 1                        # 출력 횟수 +1
            if num[1] == M:                 # 뽑은 것이 찾는 인덱스이면
                result = cnt                # 결과값에 출력 순서 저장
                break
        else:
            q.append(num)                   # 아니라면 맨 뒤로 넘기기

    print(result)