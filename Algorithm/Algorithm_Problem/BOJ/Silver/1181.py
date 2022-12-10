# 영 단어를 입력받으면 짧은 것 부터 출력
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip('\r\n')


def make_sorted_dict():
    texts = defaultdict(list)
    for _ in range(n):
        text = input()
        if text not in texts[len(text)]:    # 중복된 단어는 넣지 않음
            texts[len(text)].append(text)   # 입력받은 단어의 길이별로 저장
    return dict(sorted(texts.items()))      # 각 길이별로 저장된 단어를 사전 순서대로 정렬

n = int(input())

sorted_text = make_sorted_dict()

for i in sorted_text.values():
    for j in sorted(i):
        print(j)