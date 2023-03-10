items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]

dict1,dict2={},{}
for i in items1:
    if i[0] not in dict1  :
        dict1[i[0]]=i[1]

for i in items2:
    if i[0] not in dict2 :
        dict2[i[0]]=i[1]
l=[]
print(dict1+dict2)