n=nums.copy()
answer=0
for i in range(len(nums)-1):
    if nums[i+1]-nums[i]<=0:
        nums[i+1]=nums[i]+1
        
for i in range(len(nums)):
    answer+= (abs(nums[i]-n[i]))
print(answer)
