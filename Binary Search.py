# An array is Given

l=[1,5,8,13,15,19,23,29,31,37,41,43]
n=int(input("Enter Your Target : "))
start=0
end=len(l)-1

while start<=end:
    mid=start+(end-start)//2
    if l[mid]==n:
        print("Element Found At Index",mid)
        break
    elif l[mid]>n:
        end=mid-1
    else:
        start=mid+1
else:
    print(-1)