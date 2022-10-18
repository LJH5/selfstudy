import sys
sys.stdin = open('input.txt', 'r')
# 0~9 숫자 카드 4세트
# 6개의 카드를 골랐을 때
# run: 연속된 숫자가 3개 이상
# triplet: 같은 숫자가 3개 이상
# 플레이어 2명에서 교대로 카드를 가지고 온다
# 먼저 run이나 triplet을 만드는 사람이 승리
# 승리한 사람을 출력(1 or 2) 무승부일 경우 0을 출력
def check(player):
    for i in range(len(player)):        # triplet을 찾기
        if player[i] >= 3:              # 있으면
            return True                 # True 반환
    
    for j in range(len(player)-2):      # run을 찾기
        if player[j] >= 1 and player[j+1] >= 1 and player[j+2] >= 1: # 있으면
            return True                 # True 반환

    
T = int(input())
for tc in range(1, T+1):
    result = 0                                # 무승부면 0 출력
    card = list(map(int, input().split()))
    player1 = [0] * 10                        # player1의 숫자별 카드 개수
    player2 = [0] * 10                        # player2의 숫자별 카드 개수
    for i in range(12):                       # 카드 순서대로
        if i % 2:                             # 홀수번은 player 2
            player2[card[i]] += 1             # 해당하는 카드 개수 1 증가
            if check(player2):                # 카드 받고 run이나 triplet 이면 
                result = 2                    # player 2 승리
                break
        else:                                 # 짝수번은 player 1
            player1[card[i]] += 1             # 해당하는 카드 개수 1 증가
            if check(player1):                # 카드 받고 run이나 triplet 이면 
                result = 1                    # player 1 승리
                break

    print(f'#{tc} {result}')