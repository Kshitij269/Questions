nums = [1,2,3,4,5,6,7]
d = 3
p = 1

nums2=[0 for i in range(len(nums))]
for i in range(len(nums)):
    print(nums[(i+d+1)%len(nums)])
    nums2[i] = nums[(i+d+1)%len(nums)]
print(nums2)

