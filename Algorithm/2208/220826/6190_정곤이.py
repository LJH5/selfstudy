# 단조 증가하는 수
# 자리값비교?

# 2 4 5 6 각 숫자의 곱 중에서 최대 단조를 구하라
# 겹치는 곱하기는  set에 넣은 다음 set에 있는 곱하기는 계산하지 않는다

T = int(input())
for tc in range(1, T+1):
    result = -1
    n = int(input())
    arr = list(map(int, input().split()))
    check = []
    gop = set()
    for i in range(n):              # 중복 조합을 구한다
        for j in range(i + 1, n):
            gop.add(arr[i]*arr[j])
    for i in gop:                   # 곱한 값이 단조인지 확인
        if len(str(i)) == 1:        # 한자리수는 바로 처리
            if result < i:
                result = i
        else:
            k = int(i)
            for _ in range(len(str(i))-1):
                res = k % 10
                k //= 10
                res2 = k % 10
                if res < res2:
                    break
            else:
                if result < i:
                    result = i
    print(f'#{tc} {result}')