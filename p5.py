n=int(input("Enter the length of list: "))
list1=[]
for i in range(n):
    element=int(input("Enter the elements you want to enter: "))
    list1.append(element)
print("list of elements",list1)
search=int(input("Enter the search element:"))
if search in list1:
  print(list1.find(search))
else:
    print("-1")