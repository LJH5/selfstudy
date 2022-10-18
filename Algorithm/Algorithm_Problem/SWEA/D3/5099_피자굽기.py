import sys
sys.stdin = open('input.txt', 'r')
# n개의 피자를 동시에 굽는 화덕(queue의 크기는 n)
# m개의 피자
# 치즈의 양은 피자마다 다르다(입력받음)
# 1번 자리에서만 넣고 꺼내는 것이 가능하다(순환 queue)
# 한바퀴 돌면 치즈가 반이 녹는다 c//2
# 1번 자리에서 확인 하여 치즈 모두 녹아 0이되면 뺀다
# 뺀 자리에 남은 피자를 순서대로 넣는다
# 피자를 튜플로? (피자 번호, 녹지 않은 치즈량)
T = int(input())
for tc in range(1, T+1):
    result = 0
    n, m = map(int, input().split())                            # 화덕의 크기와 피자의 개수
    cheese_list = [0] + list(map(int, input().split()))         # 피자의 번호와 인덱스 맞추기
    pizza_num = 1                                               # 첫번째 피자
    oven = []                                                   # 화덕(queue)

    for i in range(1, n + 1):                                   # 화덕이 가득 찰 때까지
        oven.append((i, cheese_list[i]))                        # 피자를 넣는다
        pizza_num += 1                                          # 화덕에 넣지 않은 피자의 번호
    while len(oven) > 1:                                        # 화덕에 피자가 하나 남을때 까지 반복
        pizza, cheese = oven.pop(0)                             # 피자를 잠시 꺼내 치즈를 확인
        cheese //= 2                                            # 지즈는 절반 녹았고
        if cheese != 0:                                         # 치즈가 0이 아니면
            oven.append((pizza, cheese))                        # 다시 오븐에 넣는다
        elif cheese == 0 and pizza_num < m + 1:                 # 치즈가 0이고 남은 피자가 있으면
            oven.append((pizza_num, cheese_list[pizza_num]))    # 다음 피자를 넣는다
            pizza_num += 1                                      # 화덕에 넣지 않은 피자의 번호
    result = oven[0][0]                                         # 오븐에 남은 피자의 번호

    print(f'#{tc} {result}')