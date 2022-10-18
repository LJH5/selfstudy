T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    profit = 0
    n = int(input())
    sale_price = []     # 매매가를 저장할 리스트
    sale_price = list(map(int, input().split()))
    # 방법1
    # for _ in range(len(sale_price)):
    #     tmp = max(sale_price)                 # 최고 매매가 찾기
    #     index = sale_price.index(tmp)         # 최고 매매가 위치 찾기
    #     buy_sum = sum(sale_price[0:index])    # 구입 금액 = 최고 매매가 앞 매매가 다 더하기
    #     sale_sum = sale_price[index]*index    # 판매 금액 = 최고매매가 * 앞 일수
    #     profit += (sale_sum - buy_sum)        # 이익은 판매 금액 - 구입 금액
    #     del sale_price[:index+1]              # 계산한 부분은 삭제
    #     if sale_price == []:                  # 모든 매매를 진행했으면
    #         break                             # 반복문 탈출

    # 방법2(런타임 오류)
    # 뒤에서 앞으로 갈 때 작으면 차이만큼 더하기, 크면 중지
    # used = []   # 계산된 가격
    # for i in range(len(sale_price)-1, 0, -1):   # 뒤에서 부터 시작
    #     if i in used:                           # 계산된 가격이면
    #         continue                            # 이전 가격으로
    #     for j in range(i-1, -1, -1):            # 지금 가격과 이전 가격들을 비교할 거
    #         if sale_price[i] > sale_price[j]:   # 지금 가격이 이전 가격보다 높으면
    #             used.append(j)                  # 계산된 가격에 넣고
    #             profit += sale_price[i]-sale_price[j]   # 이익에 가격 차이만큼 더하기
    #         else:
    #             break

    # 방법3
    start = sale_price.pop()            # 맨뒤에 것 하나를 가져옴
    for _ in range(n-1):
        price = sale_price.pop()        # 가격을 하나 뽑아옴
        if price < start:               # 비교하여 start가 비교하는 가격보다 크면
            profit += (start-price)     # 이익에 두 가격의 차이만큼 더하기
        else:                           # 비교하여 start가 비교하는 가격보다 작으면
            start = price               # 큰 가격을 기준으로 다시 비교

    print(f'#{test_case} {profit}')