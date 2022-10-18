T = int(input())
for tc in range(1, T+1):
    result = []
    data = input()
    for i in range(len(data)//7):
        code = data[7*i:7*i+7]          # 7개씩 자르기
        tmp = 0
        for j in range(7):              # 2진수 -> 10진수
            if code[j] == '1':          # 자릿수가 1이면
                tmp += 2**(6-j)         # 자리수의 값 구하기
        result.append(tmp)
    print(*result)