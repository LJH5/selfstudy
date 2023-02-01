n = int(input())

fac = 1
for i in range(2, n+1):
    fac *= i            # 팩토리얼 구하기
cnt = 0                 # 0의 개수를 카운트할 변수
while True:
    if fac % 10:        # 10으로 나눈 나머지가 0이 아니다 == 뒷자리가 0이아니다
        print(cnt)      # 0의 개수 출력
        break           # 반복문 종료
    else:               # 10으로 나눈 나머지가 0이다 == 뒷자리가 0이다
        fac //= 10      # 10으로 나눈 몫으로 갱신 == 뒤에 0 제거
        cnt += 1        # 0의 개수 1개 올리기