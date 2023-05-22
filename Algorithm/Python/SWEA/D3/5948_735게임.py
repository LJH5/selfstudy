def perm(depth):
    global sum_list
    if depth == 3:
        if sum(sel) not in sum_list:
            sum_list.append(sum(sel))
        return

    for i in range(len(numbers)):
        if not check[i]:
            check[i] = 1
            sel[depth] = numbers[i]
            perm(depth+1)
            check[i] = 0

for tc in range(int(input())):
    numbers = list(map(int, input().split()))
    check = [0]*len(numbers)
    sel = [0]*3
    sum_list = []
    perm(0)
    sum_list.sort(reverse=True)
    result = sum_list[4]
    print(f'#{tc+1} {result}')