# 아스키 코드로 변환해서 1씩 증가해서 비교
T = int(input())
for tc in range(1, T+1):
    result = 0
    text = list(input())
    for i in range(len(text)):
        if ord(text[i]) == ord('a') + i:
            result += 1
        else:
            break
    print(f'#{tc} {result}')