nums = list(map(int, input().split()))
maxnum = 0
index = 0
for i in range(0, len(nums)):
    if int(nums[i]) >= maxnum:
        maxnum = nums[i]
        index = i
print(maxnum, index)
