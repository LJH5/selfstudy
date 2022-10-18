div_num = [2, 3, 5, 7 ,11]
cnt_list = []
n = 60
for i in div_num:
    cnt = 0 # 나눈 횟수 새기
    while n%i == 0 and n > 0: # 나머지가 0이고 n이 0보다 클때까지 실행
            n //= i    # n에 i로 나눈 값을 저장
            cnt += 1    # 나눈 횟수 +1
    cnt_list.append(cnt)
print(*cnt_list)