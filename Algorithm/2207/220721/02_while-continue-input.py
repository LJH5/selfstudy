while True:
    choice = int(input('숫자를 입력해주세요: '))   
    if choice == 4:
        print('그걸 원했어!')
        break
    elif choice in list(range(8)):
        print('아깝다')
        continue

    print('다시하자 ㅎ')