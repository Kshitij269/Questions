matrix=[[1,2,3],[4,5,6],[7,8,9]]
l=[]
row=len(matrix)
column=len(matrix[0])
count =0
total = row*column

startRow=0
startCol=0
endRow=row-1
endCol=column-1

while (count < total):
    for i in range(startCol,endCol+1):
        l.append(matrix[startRow][i])
        count+=1
    startRow+=1
        
    for j in range(startRow,endRow+1):
        l.append(matrix[endCol][j])
        count+=1
    endCol-=1

    for k in range(endCol,startCol-1,-1):
        l.append(matrix[endRow][k])
        count+=1
    endRow-=1

    for h in range(endRow,startRow-1,-1):
        l.append(matrix[h][startCol])
        count+=1
    startCol+=1

print(l)
