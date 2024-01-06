from collections import defaultdict

number = "51522623"
digit = "2"

di = defaultdict(list)
for index,value in enumerate(number):
    di[value].append(index)
ans = 0
for index in di[digit]:
    ans = max(ans,int(number[0:index]+number[index+1:len(number)]))

print(number[0:index],number[index+1:len(number)])

print(ans)