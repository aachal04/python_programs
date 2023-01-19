str=input("Enter the string:")
def findlen(str):
    count=0
    for i in str:
        count += 1
    return count
print("The length of string: ",findlen(str))