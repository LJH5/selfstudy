# 입력은 반복 실행 횟수, #테스트 번호, 문자열의 문자 총 개수, 문자열
# T만큼 반복
T = int(input())
for _ in range(T):
    # #tc와 문자 개수 n 입력 받음
    tc, n = input().split()
    #문자를 저장한 리스트
    text_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 초기 개수 0을 저장한 리스트
    cnt_list = [0] * 10
    # 문자에 해당하는 개수를 저장할 딕셔너리(문자: 키, 개수: 값)
    result_dict = dict(zip(text_list, cnt_list))
    # 문자를 하나씩 잘라 저장할 리스트
    input_list = input().split()

    # 딕셔너리의 키를 하나씩 가져옴
    for key in result_dict.keys():
        # 입력 받은 문자를 하나씩 가져옴
        for i in input_list:
            # 키와 문자가 같으면 값 1 증가
            if key == i:
                result_dict[key] += 1

    # 출력은 tc와 문자를 오름차순으로 한칸 공백을 두어 출력
    # #tc
    print(tc)
    # 키를 값만 큼 반복 출력, 뒤에 공백
    for key, value in result_dict.items():
        for _ in range(value):
            print(key, end= ' ')