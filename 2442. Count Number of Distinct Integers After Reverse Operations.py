nums=[1,13,10,12,31]
for i in range(len(nums)):
    nums.append((int(str(nums[i])[::-1])))

print(len(set(nums)))
