nums = [1,2,3,4,5]
c=[]
l=len(nums)
for i in range(l-1):
    s=nums[i]+nums[i+1]
    c.append(s)
print(False if len(set(c))==l-1 else True)
