x = [1, 4, 5, 7, 9, 6, 2, 1]
target = 7
list1= []
m=0
n=2
for i in range(len(x)):
    for j in range(i+1,len(x)):
       for k in range(j+1,len(x)):
        if (x[i] + x[j] + x[k]) == target:
            list1.append(x[i])
            list1.append(x[j])
            list1.append(x[k])
            print (x[i], x[j], x[k])