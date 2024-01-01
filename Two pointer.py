nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersection(nums1,nums2):
    i=0
    j=0
    n=len(nums1)
    m=len(nums2)
    nums1.sort()
    nums2.sort()
    res=[]
    while(i<n and j<m):
        if(nums1[i]<nums2[j]):
            i=i+1
        elif(nums2[j]<nums1[i]):
            j=j+1
        else:
            res.append(nums1[i])
            i=i+1
            j=j+1
    return list(res)

l=intersection(nums1,nums2)
print(l)
