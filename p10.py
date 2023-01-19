str1=input("Enter the String:")
str2=input("Enter the substring to search")
def searchstring(str2):
    a=str1.find(str2)
    if(a == -1):
        print("Search Unsuccessful ")
    else:
        print("Search Successful")
searchstring(str2)
