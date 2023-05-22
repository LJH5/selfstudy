# n개의 숫자로 이루어 진 수열
# m번을 회전 했을 때
# 가장 앞에 있는 숫자

T = int(input())
for tc in range(1, T+1):
    result = 0
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = arr[m % n]     # 회전하면 원래대로 되니까 m%n에 위치한 것을 출력
    print(f'#{tc} {result}')