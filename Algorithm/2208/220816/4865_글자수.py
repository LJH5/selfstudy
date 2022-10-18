T = int(input())
for tc in range(1, T+1):
    result = 0
    # 한 단어씩 분리해 set으로 저장(중복 제거)
    str1 = set(input())
    str2 = input()
    #str1의 단어를 하나씩 꺼내기
    for i in str1:
        print(i)
        # str2에 몇개 있는지 확인 후 결과값보다 크면 바꾸기
        if str2.count(i) > result:
            result = str2.count(i)

    print(f'#{tc} {result}')