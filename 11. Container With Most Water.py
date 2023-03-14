height=[1,1]
area=0
l=[]
left=0
right=len(height)-1
while left<=right:
    width=right-left
    area=min(height[left],height[right])*width
    l.append(area)
    if height[left]<height[left+1]:
        left=left+1
    else:
        right=right-1
print(max(l))
