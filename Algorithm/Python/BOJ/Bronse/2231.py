number = int(input())
if number - 9 * (len(str(number))) < 0:
    start = 1
else:
    start = number - 9 * (len(str(number)))
for i in range(start, number+1):
    if i + sum(map(int, str(i))) == number:
        print(i)
        break
    if i == number:
        print(0)

'''
91
982
9973

여기서 알아낼 수 있는 것
91 = 100 - 9*1
982 = 1000 - 9*2
9973 = 10000 - 9*3
즉 216이라면 생성자는 216 - 9*3 ~ 216 즉 189 ~ 216
'''