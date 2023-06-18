# 첫 줄에는 키의 개수 n, 퀘스트의 개수 m, 퀘스트 당 사용해야하는 스킬 수 k
# n은 10이하, k는 n이하, m은 100이하
# 스킬의 이름은 1 ~ 2n 까지
from collections import defaultdict

n, m, k = map(int, input().split())
quest_skill = defaultdict(list)
skill_cnt = [0] * (2 * n + 1)
for i in range(m):
    quest_skill[i] = list(map(int, input().split()))
    for j in quest_skill[i]:
        skill_cnt[j] += 1

print(quest_skill.values())
print(skill_cnt)