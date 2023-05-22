# 설탕배달
sugar = int(input())
ans = 0
while True:
    if sugar % 5 == 0:      # 설탕이 5의 배수이면
        ans += sugar // 5   # 5로 나눈 몫만큼 개수 증가
        sugar %= 5          # 5로 나눈 나머지로 갱신
    else:                   # 5의 배수가 아니면
        sugar -= 3          # 3빼기
        ans += 1            # 개수 1 증가

    if 0 < sugar < 3:       # 설탕이 1또는 2 만큼 남으면 
        ans = -1            # -1 출력
        break               # 반복문 종료
    elif sugar == 0:        # 설탕이 0이되면
        break               # 반복문 종료

print(ans)