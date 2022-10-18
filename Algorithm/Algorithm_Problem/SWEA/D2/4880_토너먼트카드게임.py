# 토너먼트 형식 가위, 바위, 보
# 1은 가위, 2는 바위, 3은 보
# 재귀로 풀기
# 짝수명 / 홀수명
T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    tnmt = list(map(int, input().split()))
    winner = []                 # 승자가 저장될 변수
    for i in range(n):
        winner.append(i+1)      # 승자의 번호
    for k in range(n-1):
        tmp = []
        tmp_winer = []
        for i in range(0,1 ,2 ):  # 앞에서 부터 2개씩 비교(홀수명이면 마지막 선수 부전승)
            b = tnmt.pop()
            a = tnmt.pop()
            if b - a == 1 or b - a == -2:     # 뒤가 앞을 이기는 경우
                tmp.append(b)
                tmp_winer.append(winner[i])   # 우승자 번호는 i
            else:                             # 앞이 뒤를 이기거나 비기는 경우
                tmp.append(a)
                tmp_winer.append(winner[i-1])            # 우승자 번호는 i-1
        if len(tnmt)%2:                       # 부전승자 처리
            tmp.append(tnmt.pop())
            tmp_winer.append(winner[len(tnmt)-1])
        tnmt = tmp[::-1]                      # 갱신된 대전표
        winner = tmp_winer[::-1]

    print(f'#{tc} {winner.pop()}')