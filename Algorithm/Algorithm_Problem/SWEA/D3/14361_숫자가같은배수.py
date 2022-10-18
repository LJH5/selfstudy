
# 자연수 N의 자리수를 count 배열로 개수를 센다
# N의 배수의 자리수를 comp 배열로 개수를 센다
# count와 comp를 비교
# N은 배수는 N의 자리수를 넘어가면 안 된다
T = int(input())
for tc in range(1, T+1):
    result = 'impossible'
    count = [0]*10                  # 자릿수는 0~9
    n = input()
    for i in n:
        count[int(i)] += 1
    max = len(n)
    n = int(n)
    c = 2
    while max == len(str(n)) and c < 10:
        tmp = n*c
        comp = [0]*10
        for i in str(tmp):
            comp[int(i)] += 1
        if count == comp:
            result = 'possible'
            break
        c += 1

    print(f'#{tc} {result}')
