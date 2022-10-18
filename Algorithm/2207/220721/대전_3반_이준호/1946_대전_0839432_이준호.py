#t는 테스트 케이스의 개수
t = int(input())
for i in range(t):
    #전체 문자를 all에 순서대로 저장
    all = ''
    #n은 각 테스트 케이스에 입력할 갯수
    n = int(input())
    #n_list 리스트 생성
    n_list = []
    #n_list 리스트에 2차원 배열로 입력
    for x in range(n):
        n_list.append(input().split())
    for y in range(n):
        all += (n_list[y][0]*int(n_list[y][1]))
    #테스트 케이스 번호 출력
    print(f"#{i+1}")
    #10개씩 끊어서 출력
    for z in range(0,len(all),10):
        print(all[z:z+10])