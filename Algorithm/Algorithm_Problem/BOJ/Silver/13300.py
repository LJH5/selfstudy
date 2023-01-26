# 최소 방 개수 구하기
# 학생 수 저장할 딕셔너리 만들기
import math

students_dict = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0,
                '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0}
# 방 개수
room_cnt = 0
# 사람수 방크기
students_num, room_size = map(int, input().split())

# 성별 학년 (반복)
for _ in range(students_num):
    # 문자열로 합쳐서 정보로 만들기 예) 11은 남자 1학년, 03은 여자 3학년
    student_info = input().split()
    student_info = ''.join(student_info)

    # 키를 하나씩 가져옴
    for key in students_dict:
        # 키와 학생의 정보가 같으면 학생수 1 증가
        if key == student_info:
            students_dict[key] += 1

# 방 개수 구하기 => (딕셔너리의 값 / 방크기)를 올림해서 다 더함
for value in students_dict.values():
    room_cnt += math.ceil(value/room_size)

print(room_cnt)