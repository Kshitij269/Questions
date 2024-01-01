def searchMatrix(matrix, target):
    length = len(matrix[0])
    print(length)
    low = 0
    high  = length*length - 1 
    while (high>=low):
        mid = (high+low)//2
        column = mid // length
        row =  mid % length 
        print(matrix[column][row])
        if (matrix[column][row]==target):
            return True 
        elif (matrix[column][row]>target):
            high=mid-1
        else :
            low=mid+1 
    return False 

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
searchMatrix(matrix,target)
