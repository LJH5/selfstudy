# 파일에서 데이터 읽어오기
# input() :>>> 표준입출력에서 문자열 한 줄 읽어오기
# >> 표준 입력을 콘솔 >> 파일로 변경
import sys
sys.stdin = open('input.txt', 'r')  # 파일 열기 모드 : r > 읽기, w > 쓰기

start = 2
# 리스트 앞 5개중 최대값과 위치, 두 번째로 큰 값을 찾아주는 함수
def find_max_value(index):
    max_value = 0
    second_value = 0
    max_value_index = 0
    for i in range(index, index+3):
        # 최대값과 위치, 두번째 큰 값을 찾는다
        if building_heights[i] > max_value:
            second_value = max_value
            max_value = building_heights[i]
            max_value_index = i
            # 최대값 좌우 2칸 확인 시 최대값이면 조망권을 계산한다.
    return max_value, max_value_index, second_value


find_max_value(start)


# 최대값 부터 앞까지 삭제한다.
# 최대값 오른쪽 2개는 무조건 조망권 없음, (즉 0,1 index는 무조건 조망권 없음)
# 5개 선택 값 중 0, 1 index가 최대값이라면 최대값과 앞쪽 없애기(최대값이 같아도 마찬가지로 앞쪽 최대값부터 삭제)
