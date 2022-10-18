import sys
sys.stdin = open('a.txt', 'r')

# count로 만드는 함수
def count(cards_list):
		# 카드의 숫자는 0~9
    count = [0 for _ in range(10)]
    for i in cards_list:
        count[i] += 1
    return count

# count를 받아서 run을 찾는 함수
def run(count_list):
    run_cnt = 0
    for j in range(7):
        # run 이라면 연속된 3자리에 카드가 있음
        if count_list[j] > 0 and count_list[j+1] > 0 and count_list[j+2] > 0:
            # 조합에 사용된 숫자 빼기
            count_list[j] -= 1
            count_list[j+1] -= 1
            count_list[j+2] -= 1
            run_cnt += 1
            # run이 2개라면
            if run(count_list)[1] == 1:
                run_cnt += 1
		# run을 조합한 후 남은 count_list와 run의 개수를 반환
    return (count_list, run_cnt)

# count를 받아서 triplet을 찾는 함수
def triplet(count_list):
    triplet_cnt = 0
    for j in range(10):
        # triplet이 있으면 3이상인 값이 있음
        if count_list[j] >= 3:
            # 조합된 숫자 빼기
            count_list[j] -= 3
            triplet_cnt += 1
            # triplet이 2개
            if triplet(count_list)[1] == 1:
                triplet_cnt += 1
		# triplet을 조합한 후 남은 count_list와 triplet의 개수를 반환
    return (count_list, triplet_cnt)


T = int(input())
for tc in range(1, T+1):
    # 카드는 0~9사이의 숫자 6장
    cards = input()
    cards_list = []
    for i in cards:
        cards_list.append(int(i))
		#triplet 함수를 먼저 통과한 후 run 함수 통과(triplet이 더 희귀하니까?)
    triplet_result = triplet(count(cards_list))
    run_result = run(triplet_result[0])
    if run_result[1] + triplet_result[1] == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')