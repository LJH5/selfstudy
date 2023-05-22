# 10개의 정수를 입력받고 최대와 최소를 제외한 값들의 평균을 구하시오
T = int(input())
for tc in range(1, T+1):
    result = 0
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop(0)
    arr.pop()
    result = round(sum(arr)/len(arr))
    print(f'#{tc} {result}')