# 15번 중 8번 이상 이기는 사람이 승리
# 소정이가 이기면 o, 지면 x로 표시
# 15번 경기까지 진행했을 때 점심값을 면제받을 가능성이 있는 지 판단
# 15번 중 승리한 수: w, 패배한 수: l
# 진 횟수가 7번 이하면 소정이가 승리할 수 있음
T = int(input())
for tc in range(1, T+1):
    result = 'NO'
    data = input()
    if data.count('x') <= 7:
        result = 'YES'
    print(f'#{tc} {result}')