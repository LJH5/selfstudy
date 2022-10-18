# 1~10까지의 부분집합 중 원소의 합이 10인 부분집합을 구하시오
# 부분집합의 최대 크기는 10이다
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [0]*10
res = []
def powerset(depth):
    if depth == 10:                 # 끝까지 갔으면
        tmp_sum = 0                 # 부분집합의 합을 저장할 변수
        for i in range(10):
            if check[i]:            # check가 1이면
                tmp_sum += arr[i]   # 해당하는 자리의 arr 요소를 더한다
        if tmp_sum == 10:           # 만약 부분집합의 합이 10이면
            for i in range(10):
                if check[i]:        # 해당하는 부분집합을 출력하라
                    print(arr[i], end= ' ')
            print()
        return                      # 리턴

    # 각각의 깊이에서 check는 0이거나 1이 올 수 있다
    check[depth] = 0        # 이번 자리 0선택
    powerset(depth + 1)     # 다음 자리 선택하러 가기
    check[depth] = 1        # 이번 자리 1선택
    powerset(depth + 1)     # 다음 자리 선택하러 가기

powerset(0)