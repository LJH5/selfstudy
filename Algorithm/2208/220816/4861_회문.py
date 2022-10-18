# 입력
# T
# 글자판의 길이: n 회문의 길이: m
# 문자열 (반복)
# 회문은 1개가 존재(가로, 세로)
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    txt_arr = []

    # 입력 받아서 리스트에 저장
    for i in range(n):
        txt = input()
        txt_arr.append(txt)
        # 입력 받을 때 찾기
        for j in range(n-m+1):
            if txt[j:m+j] in txt[::-1]:
                result = txt[j:m+j]
                break
            else:
                # 회문은 1개 찾으면 세로는 필요 없음
                continue

    # 세로 풀기
    # 세로 리스트 만들기 리스트 안의 요소를 문자열로 반환하고 zip하여 리스트로 만들기
    sero_list = list(zip(*txt_arr))
    # 튜플로 저장되어있는 요소 문자열로 바꾸기
    for i in range(len(sero_list)):
        sero_list[i] = ''.join(sero_list[i])
        # 입력 받을 때 찾기
        for j in range(n - m + 1):
            if sero_list[i][j:m + j] in sero_list[i][::-1]:
                result = sero_list[i][j:m + j]
                break

    print(f'#{tc} {result}')