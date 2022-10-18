# 10번 반복
# input은 tc, 찾는 문자열, 영어문장
for _ in range(10):
    tc = int(input())
    search = input()
    text = input()

    # 문자의 개수를 저장
    cnt = text.count(search)
    print(f'#{tc} {cnt}')