from collections import deque
n = int(input())

nums = deque(list(x for x in range(1, n + 1)))
# print(nums)
while len(nums) > 1:
    nums.popleft()
    num = nums.popleft()
    nums.append(num)

print(nums[-1])