import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_set = set()                    # 듣 or 보 사람의 이름을 저장할 셋
nlw = []                            # 듣보 사람의 이름을 저장할 리스트
for i in range(n+m):                # 듣 사람수 + 보 사람수
    name = input().split()[0]       # 이름을 입력받음
    if name in name_set:            # 이름이 중복된다면
        nlw.append(name)            # 듣 and 보에 저장
    else:                           # 중복되지 않으면
        name_set.add(name)          # 듣 or 보 사람에 저장

print(len(nlw))                     # 듣 and 보 사람의 수 출력
for j in sorted(nlw):               # 사전순으로 정렬된 이름
    print(j)                        # 듣 and 보 사람의 이름 출력