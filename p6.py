str=input("Enter the Expression you want:")
list1=[]
list1[:0]=str
print(list1)
l=len(list1)
if (list1[0]!=45):
    for i in list1:
        if (list1[i]==45):
            start = list1[i-1]
            end = list1[i+1]
            for j in range(start,end+1):
                print(j)
else:
    i=1
    for i in list1:
        if (list1[::]==45):
            start = list1[i-1]
            end = list1[i+1]
            for j in range(start,end+1):
                print(j)
