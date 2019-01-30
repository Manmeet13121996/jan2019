str = input('enter the str')
substr = input('enter the substr')
count =0
flag=True
start=0
while flag:
    a = str.find(substr,start)
    if a==-1:
        flag=False
    else:
        count+=1
        start=a+1
print(count)