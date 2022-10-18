# N: 총 학생 수, M: 과제를 제출한 학생의 수
for tc in range(int(input())):
    N, M = map(int, input().split())
    result = []                             # 안 낸 사람의 번호를 저장할 리스트
    check = [1]+[0]*N                       # 카운트 리스트 만들기
    for i in map(int, input().split()):     # 과제를 낸 사람의 번호와 일치하는 인덱스를 1로
        check[i] = 1

    for j in range(len(check)):
        if check[j] == 0:                   # 과제를 안 냈으면
            result.append(j)                # 과제 안 낸사람으로 저장

    print(f'#{tc+1}', *result)