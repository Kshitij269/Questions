strs = ["cba","daf","ghi"]
c = 0
for i in strs:
    if not (ord(i[0]) <= ord(i[1]) <= ord(i[2])  or ord(i[0]) >= ord(i[1]) >= ord(i[2])            ) :
        c += 1
print(c)