import sys
sys.stdin = open('input.txt', 'r')
# 조망권 확보
for tc in range(10):
    n = int(input())
    view_arr = list(map(int, input().split()))
    result = 0
    for i in range(len(view_arr)-4):
        tmp_arr = []
        for j in range(5):
            tmp_arr.append(view_arr[i+j])
        a = max(tmp_arr)    # 가장 큰 것
        if tmp_arr[2] == a:
            tmp_arr.remove(a)
            b = max(tmp_arr)    # 두번째로 큰 것
            result += (a - b)
        else:
            continue
    print(f'#{tc+1} {result}')
