emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
f=[]
for i in emails :
    l=i.split("@")
    n=l[0].split("+")
    s=n[0].replace(".","")
    f.append((s+"+"+l[1]))
print(len(set(f)))
    
    
