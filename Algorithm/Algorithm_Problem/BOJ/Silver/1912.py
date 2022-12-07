N = int(input())
nums = list(map(int, input().split()))

for i in range(1, N):   # 연속된 숫자의 합을 구해야함
    # 그 자리의 값과 그 전의 값과 합산한 것 중 큰것으로 갱신
    nums[i] = max(nums[i], nums[i - 1] + nums[i])

print(max(nums))