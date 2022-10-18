import sys
sys.stdin = open('input.txt', 'r')  # 파일 열기 모드 : r > 읽기, w > 쓰기


# 테스트 케이스 10개
for test_case in range(1, 11):
    cnt = int(input())
    box_height = list(map(int, input().split()))

    while cnt >= 0: # 횟수를 모두 소진할 때 까지 반복
        max_height = 0
        min_height = 0
        max_height_index = 0
        min_height_index = 0
        nakcha = 0

        # 가로는 항상 100고정
        # 최고 높이 찾기
        for i in range(100):
            if box_height[i] > max_height:
                max_height = box_height[i]
                max_height_index = i

        # 최저 높이 찾기 -> 최고 높이와의 낙차가 가장 큰 것
        for j in range(100):
            if max_height - box_height[j] > nakcha:
                nakcha = max_height - box_height[j]
                min_height = box_height[j]
                min_height_index = j

        # 최고 높이에서 최저 높이로 1개 이동
        box_height[max_height_index] -= 1
        box_height[min_height_index] += 1
        #
        cnt -= 1

        # 횟수 소진 전에 평준화가 된다면 반복문 종료
        if max_height - min_height <= 1:
            break


    print(f'#{test_case} {max_height - min_height}')