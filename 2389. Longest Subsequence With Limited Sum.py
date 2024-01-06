nums = [4,5,2,1]
queries = [3,10,21]

ans = []
for i in queries:
    l = len(nums)
    j=0
    print(i,sum(nums))

    if i > sum(nums):
        ans.append(l)
    else:
        print(sum(nums[j:]))
        while sum(nums[j:])>=i:
            j+=1
            print(j)
        ans.append(j)

print(ans)


