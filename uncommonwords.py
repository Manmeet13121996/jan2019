from collections import Counter
str1="geeks for geeks"
str2="learning from for geeks"

str3=""
for i in str1:
    str3=str3+i
str3=str3+ " "
for i in str2:
    str3=str3+i
list1=str3.split(' ')
c = Counter(list1)
list2 = [i for i in list1 if c[i] == 1]
str4=" ".join(list2)
print (str4)





