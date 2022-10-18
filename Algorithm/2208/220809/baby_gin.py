# run, triplet로만 구성된 경우 baby-gin
# T = int(input())
# for tc in range(1, T+1):

# 0~9의 임의의 카드 입력 6자리로 입력 받기
# number = input()
# cards_list = []
# for i in range(6):
# cards_list.append(int(number[i]))
cards_list = [1, 2, 3, 4, 5, 6]

# 3장의 카드 연속 번호 -> run을 확인하는 함수
def run(cards_list):
   run_cnt = 0
   run_check = 0 # run인지 확인하는 변수
   # set으로 중복 제거 후 list로 저장
   run_list = [num for num in set(cards_list)]
   # run_list의 요소 개수 세기

   # 오름차순 정렬
   for i in range(len(run_list)):
      for j in range(i+1, len(run_list)):
         if run_list[i] > run_list[j]:
            run_list[i], run_list[j] = run_list[j], run_list[i]

   # 처음 3개가 run인지 확인
   if run_list[0]+2 == run_list[1]+1 == run_list[2]:
      run_check += 1
   for x in range(len(run_list)):
      for y in range(x+1, len(run_list)):
         if run_list[x]+1 == run_list[x+1]:
            run_check += 1


print(run(cards_list))

# 3장의 동일한 번호 -> triplet을 확인하는 함수

