from collections import defaultdict
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    num_list = defaultdict(list)
    n = int(input())
    for i in range(1, n + 1):
        if i <= 3:
            num_list[i].append([i])
        for j in range(1, 4):
            if j < i:
                # print('-----------')
                for c in range(len(num_list[i-j])):
                    # print('i:', i, 'j:', j, 'c:', c)
                    num_list[i].append(num_list[i-j][c] + [j])

    # print(f'{n}의 조합: {len(num_list[n])}개, {num_list[n]}')
    print(len(num_list[n]))