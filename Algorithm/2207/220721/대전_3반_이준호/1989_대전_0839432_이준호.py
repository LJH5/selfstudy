#테스트 케이스 개수 t
t = int(input())
#case list 생성
case = []
#case에 2차배열로 입력
for i in range(t):
    case.append(list(input()))
#casd[0]부터 반복
for x in range(t):
    count = 0
    for y in range(len(case[x])//2):
        #양끝자리 씩 비교해서 같으면 count +1
        if case[x][y] == case[x][len(case[x])-1-y]:
            count += 1
    #비교 횟수와 count의 수가 같으면 1출력
    if count == len(case[x])//2:
        print(f"#{x+1}",1) 
    #다르면 0출력
    else:
        print(f"#{x+1}",0) 
