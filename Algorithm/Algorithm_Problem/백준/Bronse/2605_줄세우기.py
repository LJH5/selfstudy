student_cnt = int(input())
student_line = []
number = list(map(int, input().split()))

for i in range(len(number)):
    # 자신의 원래 자리수 에서 뽑은 숫자 만큼의 앞 자리에 inesrt
    student_line.insert(i-number[i], i+1)
print(*student_line)