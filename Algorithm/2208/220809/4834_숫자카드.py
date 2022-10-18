import sys
sys.stdin = open('card.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cards = input()
    cards_list = []

    for i in range(n):
        cards_list.append(int(cards[i]))

    # 0~9까지 적혀진 숫자가 주어짐
    count = [0 for _ in range(10)]

    # 가장 많은 카드의 수 카운팅 정렬을 쓰는 척하면서 안쓰기
    for j in cards_list:
        count[j] += 1

    # 값이 가장 큰 것의 인덱스가 카드의 숫자
    max_index = 0
    for x in range(10):
        # 카드의 장수가 같으면 숫자가 큰 쪽을 출력해야해서 등호를 넣음
        if count[x] >= count[max_index]:
            max_index = x

    print(f'#{test_case} {max_index} {count[max_index]}')