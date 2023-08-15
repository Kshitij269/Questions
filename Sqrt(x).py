def Sqrt(x):
    ans = -1
    low = 0
    high = x-1
    while (high>=low):
        mid = (high+low)//2
        square = mid * mid
        if square == x :
            return mid
        elif square > x :
            high = mid-1
        else :
            low = mid +1
            ans = mid

    return ans

x=int(input("Enter Number : "))
ans= Sqrt(x)
print(ans)