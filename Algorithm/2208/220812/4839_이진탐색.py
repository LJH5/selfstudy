# 페이지 이진탐색 함수
def search_page(page, page_num):
    search_cnt = 0        # 탐색 횟수
    start_page = 1      # 시작 페이지
    end_page = page     # 끝 페이지

    for i in range(page):
        center_page = int((start_page+end_page)//2)     # 중간 페이지
        search_cnt += 1                                 # 찾는 횟수 1증가
        if page_num == center_page:                     # 중간 페이지가 찾는 페이지라면
            break                                       # 반복문 종료
        elif page_num < center_page:                    # 찾는 페이지가 중간 페이지보다 작으면
            end_page = center_page                      # 끝 페이지는 중간 페이지
        else:                                           # 찾는 페이지가 중간 페이지보다 크면
            start_page = center_page                    # 시작 페이지는 중간 페이지
    return search_cnt                                   # 찾았을 때 찾는 횟수를 반환

T = int(input())
for tc in range(1, T+1):
    page, num_a, num_b = list(map(int, input().split()))

    cnt_a = search_page(page, num_a)
    cnt_b = search_page(page, num_b)

    # 찾는 횟수가 적은 사람을 출력, 같으면 0 츨력
    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')