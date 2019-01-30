word=input("enter the word")
dict1={}
s=""
for i in word:
    if i in dict1.keys():
        dict1[i]+=1
    else:
        dict1[i]=1
    if dict1[i]%3!=0:
        s=s+i
print (s)
print (dict1)