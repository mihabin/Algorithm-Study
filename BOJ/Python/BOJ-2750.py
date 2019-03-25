t = int(input())
nums = []
cnums = []
for i in range(t):
    nums.append(int(input()))
for i in range(t):
    cnums.append(min(nums))
    delnum = nums.index(min(nums))
    del(nums[delnum])
for i in range(t):
    print(cnums[i])